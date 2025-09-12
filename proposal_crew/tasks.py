# proposal_crew/tasks.py

from crewai import Task

def create_tasks(market_researcher, ai_strategist, resource_collector, proposal_writer, company_name):
    """Creates and returns all the tasks for the crew."""
    research_task = Task(
        description=f"""
            Conduct an in-depth market analysis of '{company_name}' and its primary industry.
            Your analysis must be meticulous and well-structured.

            Key areas to investigate:
            - The company's core business model, revenue streams, and key products/services.
            - Its strategic focus, competitive advantages, and market position relative to its main competitors.
            - **Crucially, find direct quotes or key statements from their most recent earnings calls,
              annual reports, or investor briefings regarding their AI, technology, and future growth strategy.**
            - Identify significant industry trends and potential challenges or opportunities for the company.

            Your final output must be a detailed, data-driven report formatted in markdown, intended for a
            strategic consultant. Include a 'References' section with links to all high-quality sources.
        """,
        expected_output="""
            A comprehensive markdown report with clearly defined sections. The report must include a dedicated
            subsection for 'Official Statements on AI/Tech Strategy' containing direct quotes or summarized
            key points from the company's official communications.
        """,
        agent=market_researcher
    )

    use_case_task = Task(
        description=f"""
            Analyze the provided market research report on '{company_name}'. Based on the report's findings,
            especially the company's official statements and identified challenges, propose a diverse
            portfolio of 4-7 high-impact AI use cases.

            Categorize each use case based on its strategic impact and implementation complexity:
            - **Operational Enhancement:** A solution to improve existing processes for immediate efficiency gains.
            - **Core Business Transformation:** A larger-scale project aimed at modernizing a fundamental part of the business.
            - **Innovative R&D Project:** A forward-thinking, exploratory initiative with the potential for significant long-term disruption.

            For each use case, you MUST provide the 'Objective', 'AI Application', and 'Cross-Functional Benefit'
            as per the required format.
        """,
        expected_output="""
            A markdown-formatted report with 4-7 use cases. Each use case must be clearly labeled
            with its category (e.g., "**Use Case 1 (Operational Enhancement): ...**") and follow the required
            three-section structure.
        """,
        agent=ai_strategist,
        context=[research_task]
    )

    resource_collection_task = Task(
        description="""
            For each of the proposed AI use cases, find high-quality, relevant resources.
            You must find at least one (or upto 6) public dataset and one open-source code repository for each use case.

            **Prioritize resources that are well-documented and show signs of community engagement
            (e.g., high star count on GitHub, recent updates, or high upvote/download count on Kaggle).**
            Your findings should be a feasibility check for a technical team.
        """,
        expected_output="""
            A markdown-formatted report. For each use case, provide a section named
            "Relevant Datasets and Repositories" with a bulleted list of high-quality, clickable markdown links.
        """,
        agent=resource_collector,
        context=[use_case_task]
    )

    report_writing_task = Task(
        description=f"""
            Synthesize all preceding information into a single, professional proposal document.
            This document is intended for the Executive Leadership and Key Stakeholders at {company_name}.

            It must be well-structured, persuasive, and formatted in markdown.
            - Start with a concise **Executive Summary** that highlights the key findings and strategic recommendations.
            - Follow with the detailed **Market Analysis**.
            - For each proposed AI use case, you must meticulously include:
                - Its strategic category (e.g., Quick Win, Strategic Initiative).
                - The "Objective/Use Case".
                - The "AI Application".
                - The "Cross-Functional Benefit".
                - The "Relevant Datasets and Repositories" with clickable links.
            - Conclude the proposal with a clear **"Recommended Next Steps"** section, outlining how the company
              could begin exploring these initiatives.
        """,
        expected_output="""
            A comprehensive and professionally formatted markdown document. It must include an
            Executive Summary, Market Analysis, detailed sections for each categorized Use Case
            (including all specified sub-points), and a final 'Recommended Next Steps' section.
            The entire report should be ready for presentation to a board of directors.
        """,
        agent=proposal_writer,
        context=[resource_collection_task]
    )
    
    return [research_task, use_case_task, resource_collection_task, report_writing_task]