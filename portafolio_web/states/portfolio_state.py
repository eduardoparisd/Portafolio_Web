import reflex as rx
from typing import TypedDict

class ProjectItem(TypedDict):
    title: str
    description: str
    category: str
    badge: str
    tags: str


class ExperienceItem(TypedDict):
    role: str
    company: str
    duration: str
    desc: str


class PortfolioState(rx.State):
    # Contact Form State
    contact_name: str = ""
    contact_email: str = ""
    contact_message: str = ""
    contact_status: str = "ENVIAR"
    is_submitting: bool = False

    # Navigation Active Tag
    active_tab: str = "home"

    # Static Data for rx.foreach (strictly formatted to avoid compile-time issues)
    projects_list: list[ProjectItem] = [
        {
            "title": "Enterprise Kubernetes Migration",
            "description": "Led zero-downtime migration of 450+ microservices from legacy VM clusters to AWS EKS with GitOps pipelines.",
            "category": "Kubernetes / AWS",
            "badge": "Infrastructure",
            "tags": "EKS, Terraform, ArgoCD, Prometheus",
        },
        {
            "title": "GitOps CI/CD Automation Engine",
            "description": "Standardized deployment pipelines across 12 product teams using reusable GitLab templates and automated canary releases.",
            "category": "CI/CD / Security",
            "badge": "Automation",
            "tags": "GitLab CI, ArgoCD, Helm, Vault",
        },
        {
            "title": "Multi-Region Multi-Cloud Mesh",
            "description": "Designed a high-availability service mesh using HashiCorp Consul across GCP and AWS environments for low-latency communications.",
            "category": "Networking",
            "badge": "Service Mesh",
            "tags": "Consul, Envoy, Terraform, VPC Peering",
        },
    ]

    experience_list: list[ExperienceItem] = [
        {
            "role": "Practicante como Administrador de Redes",
            "company": "IDAAN - Instituto de Acueductos y Alcantarillados Nacionales",
            "duration": "Octubre 2025 - Diciembre 2025",
            "desc": "Configuración y administración de dispositivos de red, despliegue de plataformas de monitoreo y gestión de inventario de red, como Nagios (monitoreo) y Netbox (DCIM), sobre sistemas Debian con servidores web Nginx y Apache",
        },
        {
            "role": "Senior Infrastructure Engineer",
            "company": "SaaSify Global",
            "duration": "2020 - 2022",
            "desc": "Maintained high availability databases and auto-scaling API clusters. Built end-to-end monitoring metrics dashboards using Prometheus and Grafana.",
        },
    ]

    skills_categories: list[dict[str, str]] = [
        {
            "name": "Orchestration", 
            "techs": "Docker"
        },
        {
            "name": "Infraestructura como Código",
            "techs": "Ansible",
        },
        {
            "name": "CI/CD & GitOps",
            "techs": "GitHub Actions",
        },
        {
            "name": "Observabilidad",
            "techs": "Prometheus, Grafana",
        },
        {
            "name": "Nube", 
            "techs": "---"
        },
    ]

    @rx.event
    async def submit_contact(self, form_data: dict):
        self.is_submitting = True
        self.contact_status = "Verifying..."
        import asyncio

        await asyncio.sleep(1.5)

        # Simple extraction
        self.contact_name = form_data.get("name", "")
        self.contact_email = form_data.get("email", "")
        self.contact_message = form_data.get("message", "")

        self.is_submitting = False
        self.contact_status = "Message Sent!"
        yield rx.toast(
            "Connection request recorded successfully!", duration=4000
        )

    @rx.event
    def select_tab(self, tab: str):
        self.active_tab = tab