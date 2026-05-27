import reflex as rx
from portafolio_web.states.portfolio_state import PortfolioState


def project_card(project: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                project["badge"],
                class_name="text-[10px] uppercase font-bold tracking-widest text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/20",
            ),
            rx.el.span(
                project["category"],
                class_name="text-xs text-slate-400 font-mono",
            ),
            class_name="flex justify-between items-center mb-4",
        ),
        rx.el.h3(
            project["title"],
            class_name="text-xl font-bold text-white mb-2 group-hover:text-emerald-300 transition-colors",
        ),
        rx.el.p(
            project["description"],
            class_name="text-slate-300 text-sm mb-4 leading-relaxed",
        ),
        rx.el.div(
            rx.el.span(
                project["tags"], class_name="text-xs text-slate-400 font-mono"
            ),
            class_name="flex flex-wrap gap-1.5 pt-2 border-t border-slate-800/80",
        ),
        class_name="group p-6 bg-slate-900/40 border border-slate-800 hover:border-emerald-500/30 transition-all duration-300 rounded-xl flex flex-col justify-between",
    )


def experience_card(exp: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    exp["role"], class_name="text-lg font-bold text-white"
                ),
                rx.el.p(
                    exp["company"],
                    class_name="text-emerald-400 font-mono text-sm",
                ),
            ),
            rx.el.span(
                exp["duration"],
                class_name="text-xs text-slate-400 font-mono px-3 py-1 bg-slate-900 border border-slate-800 rounded-full h-fit mt-1 sm:mt-0",
            ),
        ),
        rx.el.p(
            exp["desc"],
            class_name="text-slate-300 text-sm mt-3 leading-relaxed",
        ),
        class_name="p-6 bg-slate-900/30 border border-slate-800 rounded-xl relative hover:border-slate-700 transition-all",
    )


def skill_group(cat: dict) -> rx.Component:
    return rx.el.div(
        rx.el.span(
            cat["name"],
            class_name="text-xs uppercase tracking-wider font-mono text-emerald-400 font-semibold mb-2 block",
        ),
        rx.el.p(
            cat["techs"],
            class_name="text-slate-300 font-mono text-sm bg-slate-950/50 p-3 rounded-lg border border-slate-800/60 leading-relaxed",
        ),
        class_name="flex flex-col",
    )


def nav_link(label: str, target: str) -> rx.Component:
    return rx.el.a(
        label,
        href=f"#{target}",
        on_click=lambda: PortfolioState.select_tab(target),
        class_name=rx.cond(
            PortfolioState.active_tab == target,
            "text-emerald-400 font-mono text-sm transition-colors duration-200",
            "text-slate-400 hover:text-white font-mono text-sm transition-colors duration-200",
        ),
    )


def index() -> rx.Component:
    return rx.el.main(
        # Navigation Header
        rx.el.header(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "devops",
                        class_name="text-white font-bold font-mono tracking-tight text-lg",
                    ),
                    rx.el.span(
                        ".architect",
                        class_name="text-emerald-400 font-mono text-lg",
                    ),
                    class_name="flex items-center",
                ),
                # Nav Menu (Desktop)
                rx.el.nav(
                    nav_link("Sobre Mí", "sobre-mi"),
                    nav_link("Experiencia", "experiencia"),
                    nav_link("Proyectos", "proyectos"),
                    nav_link("Tecnologías", "tecnologias"),
                    nav_link("Contacto", "contacto"),
                    class_name="hidden md:flex items-center gap-6",
                ),
                # REVISAR ------------------
                rx.el.a(
                ),
                class_name="max-w-6xl mx-auto flex justify-between items-center h-16 px-4",
            ),
            class_name="fixed top-0 left-0 right-0 z-50 bg-slate-950/80 backdrop-blur-md border-b border-slate-800/80",
        ),
        # Container
        rx.el.div(
            # Hero Section
            rx.el.section(
                rx.el.div(
                    # Left: Content
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                class_name="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"
                            ),
                            rx.el.span(
                                "SYSTEM OK - DISPONIBLE PARA CONTRATOS ;)",
                                class_name="text-xs font-mono text-emerald-400 font-bold tracking-widest",
                            ),
                            class_name="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-400/5 border border-emerald-400/20 mb-6",
                        ),
                        rx.el.h1(
                            "Eduardo Paris",
                            class_name="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6",
                        ),
                        rx.el.p(
                            """Ingeniero en Sistemas Computacionales enfocado en el área de Redes, Infraestructura y DevOps. 
                            Como alguien que vive y respira NetDevOps, mi día a día no se trata de abrir sesiones de SSH para 
                            configurar manualmente cada puerto de un switch; 
                            eso lo dejé atrás. Mi trabajo se define por la orquestación.
                            """,
                            class_name="text-slate-400 text-base sm:text-lg mb-8 max-w-xl leading-relaxed",
                        ),
                        rx.el.div(
                            rx.el.a(
                                "Contáctame",
                                href="#contacto",
                                class_name="px-6 py-3 rounded-lg bg-emerald-400 text-slate-950 font-semibold hover:bg-emerald-300 transition-colors shadow-[0_0_20px_rgba(16,185,129,0.2)]",
                            ),
                            rx.el.a(
                                "Explora mis Proyectos",
                                href="#proyectos",
                                class_name="px-6 py-3 rounded-lg bg-slate-900 text-white border border-slate-800 hover:border-slate-700 transition-colors font-semibold",
                            ),
                            class_name="flex flex-wrap gap-4",
                        ),
                        class_name="flex-1",
                    ),
                    # Right: Terminal & Visual Stack
                    rx.el.div(
                        rx.el.div(
                            # Absolute circular infra graphic
                            rx.el.div(
                                class_name="absolute inset-0 bg-gradient-to-tr from-emerald-500/10 to-blue-500/10 rounded-full filter blur-2xl animate-pulse"
                            ),
                            rx.el.div(
                                rx.icon(
                                    "cpu",
                                    class_name="w-16 h-16 text-emerald-400/30 absolute top-12 left-12 animate-bounce",
                                ),
                                rx.icon(
                                    "shield-check",
                                    class_name="w-12 h-12 text-blue-400/30 absolute bottom-12 right-12",
                                ),
                                rx.el.div(
                                    rx.el.img(
                                        src="/imagen_perfil.jpg",
                                        alt="Foto de perfil",
                                        class_name="w-64 h-64 rounded-full object-cover object-bottom border-2 border-emerald-500/40 shadow-lg shadow-emerald-500/20",
                                    ),
                                    class_name="absolute inset-0 flex items-center justify-center",
                                ),
                                class_name="relative w-full aspect-square border border-slate-800 rounded-full flex items-center justify-center bg-slate-950/40",
                            ),
                            class_name="relative w-full max-w-[340px] mx-auto lg:max-w-none",
                        ),
                        class_name="flex-1 lg:max-w-[400px]",
                    ),
                    class_name="flex flex-col lg:flex-row items-center gap-12 pt-28 pb-16",
                ),
                class_name="px-4 max-w-6xl mx-auto",
            ),
            # About & Stats Section
            rx.el.section(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "SOBRE MÍ",
                            class_name="text-emerald-400 font-mono text-xs tracking-widest uppercase mb-2 block",
                        ),
                        rx.el.h2(
                            "Administrador de Redes y Automatización",
                            class_name="text-3xl font-bold text-white mb-4",
                        ),
                        rx.el.p(
                            """
                            Tengo 3 años de experiencia administrando redes y automatizando procesos de configuración de dispositivos de red. 
                            Mi red es código. Si necesito escalar la infraestructura, no me paso el día configurando dispositivos; 
                            modifico un archivo YAML, envío un pull request y dejo que el pipeline de CI/CD se encargue de probar, 
                            validar y desplegar los cambios en toda la topología de forma segura y automatizada.
                            """,
                            class_name="text-slate-300 text-sm sm:text-base leading-relaxed mb-6",
                        ),
                        # Key Metrics
                        rx.el.div(
                            rx.el.div(
                                rx.el.span(
                                    "99.99%",
                                    class_name="text-3xl font-extrabold text-white block",
                                ),
                                rx.el.span(
                                    "Average SLA Maintained",
                                    class_name="text-xs text-slate-400 font-mono",
                                ),
                                class_name="p-4 bg-slate-900/40 border border-slate-800 rounded-lg text-center",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    "50+",
                                    class_name="text-3xl font-extrabold text-white block",
                                ),
                                rx.el.span(
                                    "Pipelines Built",
                                    class_name="text-xs text-slate-400 font-mono",
                                ),
                                class_name="p-4 bg-slate-900/40 border border-slate-800 rounded-lg text-center",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    "-40%",
                                    class_name="text-3xl font-extrabold text-white block",
                                ),
                                rx.el.span(
                                    "Infrastructure Cost Cuts",
                                    class_name="text-xs text-slate-400 font-mono",
                                ),
                                class_name="p-4 bg-slate-900/40 border border-slate-800 rounded-lg text-center",
                            ),
                            class_name="grid grid-cols-1 sm:grid-cols-3 gap-4",
                        ),
                        class_name="flex-1",
                    ),
                    class_name="py-16 grid grid-cols-1 lg:grid-cols-1 gap-8",
                ),
                id="sobre-mi",
                class_name="px-4 max-w-6xl mx-auto border-t border-slate-900",
            ),
            # Experience Section (Timeline styling)
            rx.el.section(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "MI EXPERIENCIA",
                            class_name="text-emerald-400 font-mono text-xs tracking-widest uppercase mb-2 block",
                        ),
                        rx.el.h2(
                            "Work Experience",
                            class_name="text-3xl font-bold text-white mb-8",
                        ),
                        class_name="text-left",
                    ),
                    rx.el.div(
                        rx.foreach(
                            PortfolioState.experience_list, experience_card
                        ),
                        class_name="flex flex-col gap-6",
                    ),
                    class_name="py-16",
                ),
                id="experiencia",
                class_name="px-4 max-w-4xl mx-auto border-t border-slate-900",
            ),
            # Projects Section
            rx.el.section(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "AUTOMATIZACIONES",
                            class_name="text-emerald-400 font-mono text-xs tracking-widest uppercase mb-2 block",
                        ),
                        rx.el.h2(
                            "Casos de Estudios y Proyectos",
                            class_name="text-3xl font-bold text-white mb-8",
                        ),
                        class_name="text-left",
                    ),
                    rx.el.div(
                        rx.foreach(PortfolioState.projects_list, project_card),
                        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
                    ),
                    class_name="py-16",
                ),
                id="proyectos",
                class_name="px-4 max-w-6xl mx-auto border-t border-slate-900",
            ),
            # Skills Tech Stack
            rx.el.section(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "HABILIDADES",
                            class_name="text-emerald-400 font-mono text-xs tracking-widest uppercase mb-2 block",
                        ),
                        rx.el.h2(
                            "Stack de Tecnologías",
                            class_name="text-3xl font-bold text-white mb-8",
                        ),
                        class_name="text-left",
                    ),
                    rx.el.div(
                        rx.foreach(
                            PortfolioState.skills_categories, skill_group
                        ),
                        class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6",
                    ),
                    class_name="py-16",
                ),
                id="stack",
                class_name="px-4 max-w-6xl mx-auto border-t border-slate-900",
            ),
            # Contact Form Section
            rx.el.section(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "CONTÁCTAME",
                            class_name="text-emerald-400 font-mono text-xs tracking-widest uppercase mb-2 block",
                        ),
                        rx.el.h2(
                            "Colaboremos con una estrategía en la nube",
                            class_name="text-3xl font-bold text-white mb-4",
                        ),
                        rx.el.p(
                            "¿Necesitas automatizar tus implementaciones en la nube, proteger tus credenciales con Vault o migrar a Kubernetes? Completa los detalles.",
                            class_name="text-slate-400 text-sm leading-relaxed mb-6",
                        ),
                        class_name="max-w-xl mx-auto text-center",
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Nombre Completo",
                                    class_name="block text-xs font-mono uppercase text-slate-400 mb-2",
                                ),
                                rx.el.input(
                                    placeholder="Eduardo Paris",
                                    name="name",
                                    type="text",
                                    required=True,
                                    class_name="w-full bg-slate-950 border border-slate-800 focus:border-emerald-500 rounded px-4 py-3 text-white focus:outline-none transition-colors",
                                ),
                                class_name="flex-1",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Correo Electrónico",
                                    class_name="block text-xs font-mono uppercase text-slate-400 mb-2",
                                ),
                                rx.el.input(
                                    placeholder="eduardo@correo.com",
                                    name="email",
                                    type="email",
                                    required=True,
                                    class_name="w-full bg-slate-950 border border-slate-800 focus:border-emerald-500 rounded px-4 py-3 text-white focus:outline-none transition-colors",
                                ),
                                class_name="flex-1",
                            ),
                            class_name="flex flex-col sm:flex-row gap-6 mb-6",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Mensaje",
                                class_name="block text-xs font-mono uppercase text-slate-400 mb-2",
                            ),
                            rx.el.textarea(
                                #placeholder="Describe your current cloud pain points or architectural goals...",
                                name="message",
                                required=True,
                                rows=4,
                                class_name="w-full bg-slate-950 border border-slate-800 focus:border-emerald-500 rounded px-4 py-3 text-white focus:outline-none transition-colors",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.button(
                            PortfolioState.contact_status,
                            type="submit",
                            disabled=PortfolioState.is_submitting,
                            class_name="w-full py-3.5 bg-emerald-400 hover:bg-emerald-300 disabled:opacity-50 text-slate-950 font-bold rounded transition-all tracking-wider uppercase font-mono text-xs",
                        ),
                        on_submit=PortfolioState.submit_contact,
                        class_name="max-w-xl mx-auto bg-slate-900/30 border border-slate-800 p-6 sm:p-8 rounded-xl",
                    ),
                    class_name="py-16",
                ),
                id="contacto",
                class_name="px-4 max-w-6xl mx-auto border-t border-slate-900",
            ),
            # Footer
            rx.el.footer(
                rx.el.div(
                    rx.el.p(
                        "© 2026 devops.architect. All production systems simulated.",
                        class_name="text-xs text-slate-500 font-mono mb-4 sm:mb-0",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "GitHub",
                            href="#",
                            class_name="text-xs font-mono text-slate-400 hover:text-white transition-colors",
                        ),
                        rx.el.a(
                            "LinkedIn",
                            href="#",
                            class_name="text-xs font-mono text-slate-400 hover:text-white transition-colors",
                        ),
                        rx.el.a(
                            "SRE Standards",
                            href="#",
                            class_name="text-xs font-mono text-slate-400 hover:text-white transition-colors",
                        ),
                        class_name="flex gap-4",
                    ),
                    class_name="max-w-6xl mx-auto flex flex-col sm:flex-row justify-between items-center py-8 border-t border-slate-900 text-center",
                ),
                class_name="px-4",
            ),
        ),
        class_name="min-h-screen bg-slate-950 text-slate-200 font-sans",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Geist+Mono&family=Hanken+Grotesk:wght@400;500;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")