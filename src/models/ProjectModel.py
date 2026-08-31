from .BaseDataModel import BaseDataModel
from motor.motor_asyncio import AsyncIOMotorClient
from .db_schemas.project import Project
from bson.objectid import ObjectId

class ProjectModel(BaseDataModel):

    def __init__(self, db_client: AsyncIOMotorClient):
        super().__init__(db_client)
        self.collection = self.db_client["projects"]

    async def create_project(self, project: Project):
        result = await self.collection.insert_one(
            project.dict(by_alias=True, exclude_none=True)
        )
        project._id = result.inserted_id
        return project

    async def get_project_or_create(self, project_id: str):
        record = await self.collection.find_one({"project_id": project_id})
        if record is None:
            project = Project(project_id=project_id)
            project = await self.create_project(project)
            return project
        return Project(**record)

    async def get_all_projects(self, page: int = 1, page_size: int = 10):
        total_docs = await self.collection.count_documents({})
        total_pages = total_docs // page_size + (1 if total_docs % page_size > 0 else 0)

        projects = []
        cursor = self.collection.find({}).skip((page - 1) * page_size).limit(page_size)
        async for doc in cursor:
            projects.append(Project(**doc))

        return projects, total_pages
