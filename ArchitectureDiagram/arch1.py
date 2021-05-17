from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import VPC
from diagrams.aws.management import CloudformationStack
from diagrams.aws.management import Cloudformation
from diagrams.aws.management import CloudformationTemplate


graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram("HIPAA Architecture", show=True, outformat="jpg", filename="arch1", graph_attr=graph_attr, direction="TB"):
    # ELB("lb") >> EC2("web") >> RDS("userdb")
    
    # Vpc=VPC("Default Vpc")
    masterTemplate = CloudformationStack("Master")

    with Cluster("Nested Templates"):
        with Cluster("Vpc Templates"):
            vpcTemplates = [CloudformationTemplate("Management Template"), CloudformationTemplate("Production Template")]
        nestedTemplates = [ CloudformationTemplate("Application Template"), CloudformationTemplate("Config Template") , CloudformationTemplate("Logging Template"), CloudformationTemplate("IAM Template")   ]

    natTemplate = CloudformationTemplate("Nat Template")

    masterTemplate >> vpcTemplates >> natTemplate 
    masterTemplate >> nestedTemplates

    
    # CloudformationTemplate("Management Template") >> natTemplate
    # CloudformationTemplate("Production Template") >> natTemplate

    # iamTemplate=CloudformationTemplate("Iam Template")
    # loggingTemplate=CloudformationTemplate("Logging Template")

    # masterTemplate >> iamTemplate
    # masterTemplate >> loggingTemplate

# from diagrams import Diagram
# from diagrams.aws.compute import EC2

# with Diagram("Simple Diagram"):
#     EC2("web")