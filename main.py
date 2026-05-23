import os
import random

from faker import Faker
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


fake = Faker("en_IN")

OUTPUT_DIR = "generated_resumes"
os.makedirs(OUTPUT_DIR, exist_ok=True)

MIN_PDF_SIZE_KB = 11
MAX_PDF_SIZE_KB = 12

BLUE_DARK = colors.HexColor("#1B3A5C")
BLUE = colors.HexColor("#2563EB")
BLUE_LIGHT = colors.HexColor("#EFF6FF")
BLUE_BORDER = colors.HexColor("#DBEAFE")
GRAY = colors.HexColor("#6B7280")
BLACK = colors.HexColor("#111827")


CORE_SKILLS = [
    "Power BI Desktop & Service",
    "DAX & Power Query (M)",
    "SQL Server (T-SQL)",
    "SSIS / SSAS / SSRS",
    "Data Modelling (Star Schema)",
    "ETL Pipeline Design",
    "KPI Design & Monitoring",
    "Azure Data Services",
    "Advanced Excel & VBA",
    "Power BI Gateway",
    "Paginated Reports",
    "Row-Level Security (RLS)",
]

SKILL_ALIASES = {
    "power bi": "Power BI Desktop & Service",
    "dax": "DAX & Power Query (M)",
    "power query": "DAX & Power Query (M)",
    "sql server": "SQL Server (T-SQL)",
    "t-sql": "SQL Server (T-SQL)",
    "ssis": "SSIS / SSAS / SSRS",
    "ssas": "SSIS / SSAS / SSRS",
    "ssrs": "SSIS / SSAS / SSRS",
    "excel": "Advanced Excel & VBA",
    "azure": "Azure Data Services",
    "etl": "ETL Pipeline Design",
    "dashboard": "KPI Design & Monitoring",
    "reports": "Paginated Reports",
}

EXPERIENCE_POINTS = [
    "Architected and deployed 15+ Power BI dashboards consuming data from SQL Server DW, Azure SQL, and REST APIs, reducing manual reporting effort by 40%.",
    "Designed star-schema data models with fact and dimension tables; implemented row-level security for regional business units.",
    "Authored advanced DAX measures including YTD, MTD, rolling 12-month trends, dynamic KPI scorecards, and variance analysis.",
    "Redesigned legacy SSIS packages to optimize incremental loads, improve error handling, and cut ETL runtime by 35%.",
    "Defined KPIs with Sales, Finance, and Operations stakeholders and configured automated refresh schedules in Power BI Service.",
    "Maintained SSAS Tabular models and created SSRS paginated reports for finance, operations, and compliance teams.",
    "Developed T-SQL stored procedures, views, and CTEs to pre-aggregate data for reporting layers, improving query performance by 50%.",
    "Produced technical specifications, data-flow diagrams, release notes, and user manuals for delivered BI assets.",
    "Built Power Query transformations and parameter-driven reports that eliminated recurring manual data preparation steps.",
    "Led peer reviews, validated report accuracy with source-system owners, and onboarded junior analysts on BI delivery standards.",
]

PROJECTS = [
    {
        "name": "Enterprise Sales Performance Hub",
        "stack": "Power BI | SQL Server | SSIS | DAX",
        "summary": "Consolidated CRM, ERP, and flat-file data into a unified SQL Server warehouse and built an 8-page Power BI suite covering pipeline, revenue, and rep performance. Reduced monthly close reporting from 3 days to 4 hours.",
    },
    {
        "name": "Finance Operations Dashboard",
        "stack": "Power BI | SSAS | Azure SQL",
        "summary": "Designed a finance dashboard using Azure SQL and SSAS models; implemented DAX KPIs for budget vs. actuals, cash-flow variance, and aging receivables used by controllers daily.",
    },
    {
        "name": "HR Analytics Platform",
        "stack": "Power BI | SQL Server | SSRS",
        "summary": "Developed workforce analytics dashboards with department-level security and complementary SSRS reports for payroll and compliance tracking.",
    },
    {
        "name": "Operations KPI Command Center",
        "stack": "Power BI | Power Query | SQL Server",
        "summary": "Created operational dashboards for SLA, volume, backlog, and productivity metrics with automated refreshes and executive-level bookmarks.",
    },
    {
        "name": "Retail Revenue Analytics Suite",
        "stack": "Power BI | Azure SQL | DAX",
        "summary": "Built sales, inventory, and margin dashboards for retail leadership with drill-through pages by region, store, category, and sales channel.",
    },
    {
        "name": "Supply Chain Visibility Dashboard",
        "stack": "Power BI | SQL Server | Power Query",
        "summary": "Created supplier, logistics, and delivery performance reports that helped operations teams track delays, fill rates, and inventory risk.",
    },
    {
        "name": "Customer Churn Insights Model",
        "stack": "Power BI | Python | SQL Server",
        "summary": "Prepared customer datasets and designed executive dashboards showing churn indicators, revenue leakage, and segment-level retention actions.",
    },
    {
        "name": "Executive KPI Scorecard",
        "stack": "Power BI | SSAS | DAX",
        "summary": "Designed a leadership scorecard with KPI thresholds, trend indicators, and automated refreshes for monthly business review meetings.",
    },
    {
        "name": "Claims Reporting Modernization",
        "stack": "Power BI | SSRS | SQL Server",
        "summary": "Migrated legacy Excel and SSRS reports into interactive Power BI dashboards with validated measures and governed access controls.",
    },
    {
        "name": "Manufacturing Quality Analytics",
        "stack": "Power BI | SQL Server | Power Query",
        "summary": "Delivered quality, rejection, downtime, and production dashboards with plant-level filters and root-cause views for process owners.",
    },
]

COMPANIES = [
    "TechNova Solutions Pvt. Ltd.",
    "Infovision Analytics",
    "DataVista Consulting",
    "NexGen Insights",
    "BluePeak Technologies",
    "QuantEdge Analytics",
    "Visionary Data Labs",
    "CloudMetric Solutions",
    "InsightWorks Technologies",
    "DataBridge Systems",
    "Apex BI Services",
    "NextWave Digital",
]

ROLE_PROFILES = [
    {
        "title": "Business Intelligence Developer",
        "current_roles": ["Power BI Developer", "BI Developer", "Business Intelligence Developer"],
        "previous_roles": ["Junior BI Developer", "Data Analyst", "Reporting Analyst"],
        "years": random.choice([3, 4, 5]),
    },
    {
        "title": "Power BI Developer",
        "current_roles": ["Power BI Developer", "BI Analyst", "BI Reporting Developer"],
        "previous_roles": ["MIS Analyst", "SQL Reporting Analyst", "Data Analyst"],
        "years": random.choice([2, 3, 4]),
    },
    {
        "title": "Senior BI Developer",
        "current_roles": ["Senior BI Developer", "Senior Power BI Developer", "BI Consultant"],
        "previous_roles": ["BI Developer", "Power BI Analyst", "SQL BI Developer"],
        "years": random.choice([5, 6, 7]),
    },
    {
        "title": "Data Visualization Developer",
        "current_roles": ["Data Visualization Developer", "Power BI Consultant", "Analytics Developer"],
        "previous_roles": ["Reporting Analyst", "Data Analyst", "Power BI Analyst"],
        "years": random.choice([3, 4, 5]),
    },
]

TEAMS = [
    "Full-time | Analytics Practice",
    "Full-time | Data & Insights Team",
    "Full-time | Enterprise Reporting",
    "Full-time | Business Analytics COE",
    "Full-time | Data Platform Team",
    "Contract | BI Modernization Program",
]

EDUCATION_OPTIONS = [
    ("Bachelor of Engineering - Computer Science", "Savitribai Phule Pune University"),
    ("Bachelor of Technology - Information Technology", "Rashtrasant Tukadoji Maharaj Nagpur University"),
    ("Bachelor of Science - Computer Science", "University of Mumbai"),
    ("Master of Computer Applications", "Pune University"),
    ("Bachelor of Engineering - Electronics & Telecommunication", "Nagpur University"),
    ("Bachelor of Computer Applications", "Bangalore University"),
]

CERTIFICATION_POOL = [
    "Microsoft Certified: Power BI Data Analyst Associate (PL-300)",
    "Microsoft Certified: Azure Data Fundamentals (DP-900)",
    "Microsoft Certified: Azure Database Administrator Associate (DP-300)",
    "Microsoft Certified: Azure Fundamentals (AZ-900)",
    "Microsoft Certified: Fabric Analytics Engineer Associate (DP-600)",
    "SQL Server Reporting Services Certification",
    "Advanced DAX for Power BI",
    "Power BI Service Administration",
    "Data Warehousing and Business Intelligence",
    "Excel Power Pivot and Power Query Certification",
]

ADDITIONAL_SKILL_POOL = [
    "Reporting & Visualisation: Power BI Desktop, Power BI Service, SSRS, Paginated Reports, Custom Visuals",
    "Data Platforms: SQL Server 2016/2019, Azure Synapse Analytics, Azure SQL Database, Azure Data Factory",
    "Programming & Query: T-SQL, DAX, Power Query M, Python (pandas, openpyxl), basic VBA",
    "Data Warehousing: Kimball methodology, Star & Snowflake schema, SCD Types 1 & 2",
    "Productivity: Advanced Excel, Power Pivot, SharePoint, Teams, Jira",
    "Governance: Workspace management, data refresh monitoring, access control, deployment pipelines",
    "Analytics: KPI design, variance analysis, forecasting support, executive scorecards",
    "Data Integration: Flat files, REST APIs, Oracle, SQL Server, cloud data sources",
    "Documentation: Data dictionaries, report catalogs, user guides, release notes",
    "Quality: Report validation, reconciliation, UAT support, stakeholder sign-off",
]

SUMMARY_TEMPLATES = [
    "{title} with {years}+ years of experience building dashboards, semantic models, and reporting solutions across {domain}. Skilled in {skills}, requirement analysis, and stakeholder communication.",
    "Detail-oriented {title} with {years}+ years of hands-on experience in {skills}. Strong background in transforming raw operational data into governed dashboards and decision-ready insights for {domain}.",
    "Analytics-focused {title} with {years}+ years of experience delivering Power BI reports, DAX measures, SQL datasets, and KPI scorecards. Known for improving reporting accuracy, refresh reliability, and executive visibility.",
    "Business-minded {title} with {years}+ years of experience converting business questions into scalable BI solutions. Experienced in {skills}, data modelling, dashboard design, and report performance tuning.",
]

DOMAINS = [
    "sales and finance teams",
    "operations and supply-chain functions",
    "HR, finance, and leadership teams",
    "retail, manufacturing, and service operations",
    "enterprise reporting and KPI governance",
    "customer analytics and revenue operations",
]


def build_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=26,
            leading=30,
            textColor=colors.white,
            spaceAfter=4,
        ),
        "header_title": ParagraphStyle(
            "HeaderTitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=12,
            leading=15,
            textColor=colors.white,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=11,
            textColor=colors.white,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=BLUE_DARK,
            borderColor=BLUE,
            borderWidth=0,
            borderPadding=0,
            spaceBefore=10,
            spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            textColor=BLACK,
            spaceAfter=4,
        ),
        "body_gray": ParagraphStyle(
            "BodyGray",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=GRAY,
            spaceAfter=4,
        ),
        "item_title": ParagraphStyle(
            "ItemTitle",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.2,
            leading=13,
            textColor=BLACK,
            spaceBefore=3,
            spaceAfter=1,
        ),
        "skill": ParagraphStyle(
            "Skill",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8.6,
            leading=10.5,
            textColor=BLUE_DARK,
            alignment=TA_CENTER,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=10,
            textColor=GRAY,
            alignment=TA_CENTER,
            spaceBefore=8,
        ),
    }


def extract_skills(jd):
    jd_lower = jd.lower()
    found = []
    for key, skill in SKILL_ALIASES.items():
        if key in jd_lower and skill not in found:
            found.append(skill)
    for skill in CORE_SKILLS:
        if skill.lower() in jd_lower and skill not in found:
            found.append(skill)
    for skill in CORE_SKILLS:
        if len(found) >= 9:
            break
        if skill not in found:
            found.append(skill)
    required = found[:3]
    optional = found[3:] + [skill for skill in CORE_SKILLS if skill not in found]
    random.shuffle(optional)
    return (required + optional)[:9]


def generate_summary(title, years, skills):
    lead_skills = ", ".join(skills[:4])
    template = random.choice(SUMMARY_TEMPLATES)
    return template.format(
        title=title,
        years=years,
        skills=lead_skills,
        domain=random.choice(DOMAINS),
    )


def generate_experience_points(skills, senior=False):
    dashboard_count = random.choice([6, 8, 10, 12, 15, 18, 20])
    user_count = random.choice([80, 120, 150, 200, 250, 300])
    reporting_gain = random.choice([25, 30, 35, 40, 45, 50])
    etl_gain = random.choice([20, 25, 30, 35, 40])
    performance_gain = random.choice([30, 35, 40, 45, 50, 55])
    source = random.choice(["SQL Server", "Azure SQL", "Oracle", "Excel files", "REST APIs", "Azure Synapse"])
    department = random.choice(["Sales", "Finance", "Operations", "HR", "Supply Chain", "Customer Success"])
    model = random.choice(["star-schema", "snowflake", "tabular", "semantic"])

    pool = [
        f"Built {dashboard_count}+ Power BI dashboards using data from {source}, improving recurring reporting turnaround by {reporting_gain}%.",
        f"Designed {model} data models and reusable DAX measures for {department} KPIs, improving consistency across business reports.",
        f"Created Power Query transformations and SQL views that reduced manual data preparation effort for {user_count}+ users.",
        f"Optimized report queries, relationships, and measures, improving dashboard load performance by {performance_gain}%.",
        f"Configured Power BI Service refresh schedules, workspace access, and row-level security for business teams.",
        f"Partnered with {department} stakeholders to gather requirements, validate calculations, and deliver actionable KPI scorecards.",
        f"Developed T-SQL stored procedures, CTEs, and reporting datasets for faster Power BI and SSRS consumption.",
        f"Redesigned ETL workflows and validation checks, reducing data refresh failures and cutting processing time by {etl_gain}%.",
        f"Prepared report documentation, metric definitions, and user guides to improve adoption across {department} teams.",
        f"Delivered UAT support, reconciled dashboard totals with source systems, and managed production report releases.",
    ]
    if senior:
        pool.extend(
            [
                "Reviewed BI deliverables from junior analysts and introduced dashboard design standards for the reporting team.",
                "Led stakeholder demos and sprint planning for BI enhancements across multiple business units.",
                "Created reusable Power BI templates and measure patterns to speed up report delivery.",
            ]
        )
    return random.sample(pool, 4)


def generate_duration_pair(years):
    current_start_year = 2026 - random.choice([1, 2, 3])
    previous_start_year = max(2018, current_start_year - random.choice([1, 2, 3]))
    previous_end_year = current_start_year - 1
    current_month = random.choice(["Jan", "Mar", "Apr", "Jul", "Sep", "Nov"])
    previous_month = random.choice(["Jan", "Feb", "Jun", "Jul", "Aug", "Oct"])
    end_month = random.choice(["Mar", "Jun", "Sep", "Dec"])

    if years <= 3:
        previous_start_year = current_start_year - 1
    return (
        f"{current_month} {current_start_year} - Present",
        f"{previous_month} {previous_start_year} - {end_month} {previous_end_year}",
    )


def generate_projects():
    projects = []
    for project in random.sample(PROJECTS, 3):
        summary = project["summary"]
        summary = summary.replace("3 days", random.choice(["2 days", "3 days", "4 days"]))
        summary = summary.replace("4 hours", random.choice(["3 hours", "4 hours", "6 hours"]))
        projects.append(
            {
                "name": project["name"],
                "stack": project["stack"],
                "summary": summary,
            }
        )
    return projects


def generate_resume_data(jd):
    first = fake.unique.first_name_male()
    last = fake.last_name()
    profile = random.choice(ROLE_PROFILES)
    skills = extract_skills(jd)
    company_one, company_two = random.sample(COMPANIES, 2)
    city = random.choice(["Pune", "Nagpur", "Mumbai", "Bengaluru", "Hyderabad"])
    years = profile["years"]
    current_duration, previous_duration = generate_duration_pair(years)
    education, university = random.choice(EDUCATION_OPTIONS)
    senior = years >= 5

    return {
        "name": f"{first} {last}",
        "title": profile["title"],
        "email": f"{first.lower()}.{last.lower()}@email.com",
        "phone": f"+91 {random.randint(70000, 99999)} {random.randint(10000, 99999)}",
        "location": f"{city}, Maharashtra" if city in ["Pune", "Nagpur", "Mumbai"] else city,
        "linkedin": f"linkedin.com/in/{first.lower()}{last.lower()}",
        "summary": generate_summary(profile["title"], years, skills),
        "skills": skills,
        "experiences": [
            {
                "role": random.choice(profile["current_roles"]),
                "company": company_one,
                "team": random.choice(TEAMS),
                "duration": current_duration,
                "points": generate_experience_points(skills, senior=senior),
            },
            {
                "role": random.choice(profile["previous_roles"]),
                "company": company_two,
                "team": random.choice(TEAMS),
                "duration": previous_duration,
                "points": generate_experience_points(skills, senior=False),
            },
        ],
        "projects": generate_projects(),
        "education": education,
        "university": university,
        "education_years": random.choice(["2016 - 2020", "2017 - 2021", "2018 - 2022", "2015 - 2019"]),
        "certifications": random.sample(CERTIFICATION_POOL, 3),
        "additional_skills": random.sample(ADDITIONAL_SKILL_POOL, 5),
    }


def add_section(story, title, styles):
    story.append(Spacer(1, 4))
    story.append(Paragraph(title, styles["section"]))
    story.append(
        Table(
            [[""]],
            colWidths=[7.0 * inch],
            rowHeights=[1.4],
            style=[("BACKGROUND", (0, 0), (-1, -1), BLUE)],
        )
    )
    story.append(Spacer(1, 5))


def build_header(data, styles):
    left = [
        Paragraph(data["name"].upper(), styles["name"]),
        Paragraph(data["title"], styles["header_title"]),
    ]
    right = [
        Paragraph(data["email"], styles["contact"]),
        Paragraph(data["phone"], styles["contact"]),
        Paragraph(data["location"], styles["contact"]),
        Paragraph(data["linkedin"], styles["contact"]),
    ]
    table = Table([[left, right]], colWidths=[5.05 * inch, 1.95 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), BLUE_DARK),
                ("BACKGROUND", (1, 0), (1, 0), BLUE),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (0, 0), 14),
                ("RIGHTPADDING", (0, 0), (0, 0), 8),
                ("TOPPADDING", (0, 0), (0, 0), 12),
                ("BOTTOMPADDING", (0, 0), (0, 0), 12),
                ("LEFTPADDING", (1, 0), (1, 0), 10),
                ("RIGHTPADDING", (1, 0), (1, 0), 10),
                ("TOPPADDING", (1, 0), (1, 0), 9),
                ("BOTTOMPADDING", (1, 0), (1, 0), 9),
            ]
        )
    )
    return table


def build_skills_table(skills, styles):
    rows = []
    for index in range(0, len(skills), 3):
        row = skills[index:index + 3]
        while len(row) < 3:
            row.append("")
        rows.append([Paragraph(skill, styles["skill"]) for skill in row])

    table = Table(rows, colWidths=[2.33 * inch, 2.33 * inch, 2.33 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), BLUE_LIGHT),
                ("BOX", (0, 0), (-1, -1), 0.6, BLUE_BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.6, BLUE_BORDER),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def bullet_list(points, styles):
    return ListFlowable(
        [
            ListItem(Paragraph(point, styles["body"]), leftIndent=10)
            for point in points
        ],
        bulletType="bullet",
        start="circle",
        leftIndent=14,
        bulletFontName="Helvetica",
        bulletFontSize=7,
    )


def pad_pdf_to_target_size(filename, min_kb=MIN_PDF_SIZE_KB, max_kb=MAX_PDF_SIZE_KB):
    min_bytes = min_kb * 1024
    max_bytes = max_kb * 1024
    current_size = os.path.getsize(filename)

    if current_size >= min_bytes:
        return current_size

    target_size = random.randint(min_bytes, max_bytes)
    padding_size = target_size - current_size
    padding = b"\n%" + (b" " * max(0, padding_size - 3)) + b"\n"

    with open(filename, "ab") as file:
        file.write(padding)

    return os.path.getsize(filename)


def create_pdf_resume(data, filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
    )
    styles = build_styles()
    story = [build_header(data, styles), Spacer(1, 8)]

    add_section(story, "Professional Summary", styles)
    story.append(Paragraph(data["summary"], styles["body"]))

    add_section(story, "Core Technical Skills", styles)
    story.append(build_skills_table(data["skills"], styles))

    add_section(story, "Professional Experience", styles)
    for exp in data["experiences"]:
        story.append(
            KeepTogether(
                [
                    Paragraph(
                        f"<b>{exp['role']}</b> | {exp['company']}",
                        styles["item_title"],
                    ),
                    Paragraph(
                        f"{exp['team']} &nbsp;&nbsp;&nbsp;&nbsp; {exp['duration']}",
                        styles["body_gray"],
                    ),
                ]
            )
        )
        story.append(bullet_list(exp["points"], styles))

    add_section(story, "Key Projects", styles)
    for project in data["projects"]:
        story.append(
            KeepTogether(
                [
                    Paragraph(project["name"], styles["item_title"]),
                    Paragraph(f"| {project['stack']}", styles["body_gray"]),
                    Paragraph(project["summary"], styles["body"]),
                ]
            )
        )

    add_section(story, "Education", styles)
    story.append(
        Paragraph(
            f"<b>{data['education']}</b> &nbsp;&nbsp;&nbsp;&nbsp; "
            f"<font color='#6B7280'>{data['education_years']}</font>",
            styles["body"],
        )
    )
    story.append(Paragraph(data["university"], styles["body_gray"]))

    add_section(story, "Certifications", styles)
    story.append(bullet_list(data["certifications"], styles))

    add_section(story, "Additional Skills & Tools", styles)
    for skill in data["additional_skills"]:
        story.append(Paragraph(skill, styles["body"]))

    story.append(Paragraph("References available upon request", styles["footer"]))
    doc.build(story)
    pad_pdf_to_target_size(filename)


def main():
    print("=" * 60)
    print("BUSINESS INTELLIGENCE PDF RESUME GENERATOR")
    print("=" * 60)

    jd_path = os.path.join(OUTPUT_DIR, "jd.txt")
    with open(jd_path, "r", encoding="utf-8") as file:
        jd = file.read()

    count = int(input("\nHow many resumes to generate (1-100): "))
    if count < 1 or count > 100:
        print("Please enter a number between 1 and 100")
        return

    for i in range(count):
        data = generate_resume_data(jd)
        filename = os.path.join(OUTPUT_DIR, f"bi_developer_resume_{i + 1}.pdf")
        create_pdf_resume(data, filename)
        print(f"Generated: {filename}")

    print("\nBI-style PDF resumes generated successfully!")


if __name__ == "__main__":
    main()
