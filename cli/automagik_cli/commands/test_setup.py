import uuid
import click
from sqlalchemy.orm import Session
from core.database.models import Task, FlowDB
from core.database import get_db_session

@click.command()
def setup_test_tasks():
    """Create test tasks for development"""
    session = get_db_session()
    
    # Create a test flow
    flow = FlowDB(
        id=uuid.uuid4(),
        name="Test Flow",
        description="A test flow for development",
        source="local",
        source_id="test",
        input_component="input-123",
        output_component="output-456",
        data={"nodes": [], "edges": []}
    )
    session.add(flow)
    session.commit()
    
    # Create test tasks
    for i in range(3):
        task = Task(
            flow_id=flow.id,
            input_data={"test": f"input {i}"},
            status="pending"
        )
        session.add(task)
    
    session.commit()
    click.echo("Created test flow and tasks")