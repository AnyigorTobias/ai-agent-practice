from phi.knowledge.website import WebsiteKnowledgeBase
from phi.vectordb.pgvector import PgVector


db_url = "postgresql+psycopg://admin:admin@localhost:5532/webdocs"



knowledge_base = WebsiteKnowledgeBase(
    urls=["https://opportunitydesk.org/"],
    # Number of links to follow from the seed URLs
    # Number of links to follow from the seed URLs
    max_links=10,
    # Table name: ai.website_documents
    vector_db=PgVector(
        table_name="website_documents",
        db_url= db_url,
    ),
)