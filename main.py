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
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


fake = Faker("en_IN")

OUTPUT_DIR = "generated_resumes"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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
]

COMPANIES = [
    "TechNova Solutions Pvt. Ltd.",
    "Infovision Analytics",
    "DataVista Consulting",
    "NexGen Insights",
    "BluePeak Technologies",
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
    return found[:9]


def generate_summary(skills):
    lead_skills = ", ".join(skills[:4])
    return (
        "Results-driven Business Intelligence Developer with hands-on experience designing "
        "and delivering enterprise-grade analytics solutions. Proven expertise in "
        f"{lead_skills}, data modelling, and ETL workflows. Adept at translating business "
        "requirements into actionable dashboards that improve reporting speed, KPI visibility, "
        "and strategic decision-making."
    )


def generate_resume_data(jd):
    first = fake.first_name_male()
    last = fake.last_name()
    skills = extract_skills(jd)
    company_one, company_two = random.sample(COMPANIES, 2)
    city = random.choice(["Pune", "Nagpur", "Mumbai", "Bengaluru", "Hyderabad"])

    return {
        "name": f"{first} {last}",
        "title": "Business Intelligence Developer",
        "email": f"{first.lower()}.{last.lower()}@email.com",
        "phone": f"+91 {random.randint(70000, 99999)} {random.randint(10000, 99999)}",
        "location": f"{city}, Maharashtra" if city in ["Pune", "Nagpur", "Mumbai"] else city,
        "linkedin": f"linkedin.com/in/{first.lower()}{last.lower()}",
        "summary": generate_summary(skills),
        "skills": skills,
        "experiences": [
            {
                "role": random.choice(["Senior BI Developer", "Power BI Developer", "BI Developer"]),
                "company": company_one,
                "team": "Full-time | Analytics Practice",
                "duration": "Jan 2023 - Present",
                "points": random.sample(EXPERIENCE_POINTS, 6),
            },
            {
                "role": random.choice(["BI Developer", "Power BI Analyst", "Data Analyst"]),
                "company": company_two,
                "team": "Full-time | Data & Insights Team",
                "duration": "Jul 2021 - Dec 2022",
                "points": random.sample(EXPERIENCE_POINTS, 5),
            },
        ],
        "projects": random.sample(PROJECTS, 3),
        "education": "Bachelor of Engineering - Computer Science",
        "university": "Savitribai Phule Pune University",
        "education_years": "2017 - 2021",
        "certifications": [
            "Microsoft Certified: Power BI Data Analyst Associate (PL-300)",
            "Microsoft Certified: Azure Data Fundamentals (DP-900)",
            "Microsoft Certified: Azure Database Administrator Associate (DP-300)",
        ],
        "additional_skills": [
            "Reporting & Visualisation: Power BI Desktop, Power BI Service, SSRS, Paginated Reports, Custom Visuals",
            "Data Platforms: SQL Server 2016/2019, Azure Synapse Analytics, Azure SQL Database, Azure Data Factory",
            "Programming & Query: T-SQL, DAX, Power Query M, Python (pandas, openpyxl), basic VBA",
            "Data Warehousing: Kimball methodology, Star & Snowflake schema, SCD Types 1 & 2",
            "Productivity: Advanced Excel, Power Pivot, SharePoint, Teams, Jira",
        ],
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

    story.append(PageBreak())
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


def main():
    print("=" * 60)
    print("BUSINESS INTELLIGENCE PDF RESUME GENERATOR")
    print("=" * 60)

    jd_path = os.path.join(OUTPUT_DIR, "jd.txt")
    with open(jd_path, "r", encoding="utf-8") as file:
        jd = file.read()

    count = int(input("\nHow many resumes to generate (3-5): "))
    if count < 3 or count > 5:
        print("Please enter a number between 3 and 5")
        return

    for i in range(count):
        data = generate_resume_data(jd)
        filename = os.path.join(OUTPUT_DIR, f"bi_developer_resume_{i + 1}.pdf")
        create_pdf_resume(data, filename)
        print(f"Generated: {filename}")

    print("\nBI-style PDF resumes generated successfully!")


if __name__ == "__main__":
    main()
