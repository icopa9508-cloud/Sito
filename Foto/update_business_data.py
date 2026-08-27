# Script to update Business in IRELAND_SUBJECTS and CURATED_CONCEPT_TOPICS from BUSINESS.docx
import re

html_path = r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html'
with open(html_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Business in IRELAND_SUBJECTS
old_business_start = '        id: "business",'
old_accounting_start = '        id: "accounting",'

before_biz = code.split(old_business_start)[0]
after_biz = old_accounting_start + code.split(old_accounting_start)[1]

new_business = """        id: "business",
        name: "Business",
        type: "Commerce",
        image: IMAGES.subjects.business,
        summary: "Comprehensive study of commercial enterprise: people in business, management and leadership theories, market research, marketing mix (4 Ps), domestic economy, corporate finance, and international global trade.",
        keywords: ["Stakeholders", "Motivation & Leadership", "Marketing Mix (4 Ps)", "Global Trade & MNCs"],
        topics: [
          "People in Business & Conflict Resolution",
          "Management: Motivating, Communicating & Leadership",
          "Marketing: Market Research & The Marketing Mix",
          "Domestic Environment: Business, Economy & CSR",
          "Finance: Sources of Finance, Cash Flow & Budgeting",
          "International Business: EU, Global Trade & Multinationals"
        ],
        reflection: "Mastering commercial decision-making: analyzing stakeholder dynamics, developing marketing strategies, evaluating financial risk, and navigating international trade environments.",
        detailedTopics: [
          {
            title: "People in Business & Conflict Resolution",
            desc: "Introduction to the business world: enterprise purpose and satisfying customer needs. Comprehensive analysis of key stakeholders (owners, employees, customers, suppliers, government, local community) and competing interests (profit vs. wages, growth vs. environmental protection). Conflict resolution frameworks: non-legal methods (negotiation, conciliation), mediation, and legal action (Workplace Relations Commission, Labour Court). Defining employment relationships through legally binding contracts, statutory rights, employer duties, and the role of trade unions."
          },
          {
            title: "Management: Motivating, Communicating & Leadership",
            desc: "Core management activities: motivation theories (Maslow's Hierarchy of Needs, Herzberg's Hygiene Factors and Motivators, Taylor's Scientific Management, Mayo's Human Relations). Evaluating leadership paradigms (autocratic, democratic, laissez-faire, situational). Effective business communication (internal/external, formal/informal, verbal/non-verbal), identifying communication barriers (noise, jargon, prejudice), leveraging ICT (intranet, video conferencing, enterprise platforms), and managing organizational resistance to change."
          },
          {
            title: "Marketing: Market Research & The Marketing Mix",
            desc: "Identifying and satisfying customer needs profitably. Primary (field) research (questionnaires, in-depth interviews, focus groups, observation) vs. Secondary (desk) research (CSO census data, industry reports, competitor intelligence), sampling methods, and research ethics. Strategic implementation of the Marketing Mix (4 Ps): Product (product life cycle, differentiation, branding, packaging), Price (penetration, skimming, competitive, psychological pricing), Place (distribution channels, logistics, supply chain), and Promotion (advertising, PR, sales promotion, digital marketing/SEO) plus extended 3 Ps for services (People, Process, Physical Evidence)."
          },
          {
            title: "Domestic Environment: Business, Economy & CSR",
            desc: "Business operation across economic sectors: Primary (agriculture/fishing), Secondary (manufacturing/industry), Tertiary (services), and Quaternary (ICT/R&D). Comparing business legal structures: sole traders, partnerships, private limited companies (Ltd), public limited companies (PLC), cooperatives, and social enterprises. Macroeconomic impact on business: inflation, interest rates, taxation, unemployment, and GDP growth. Government economic intervention and Corporate Social Responsibility (CSR): ethical standards, environmental sustainability, and local community impact."
          },
          {
            title: "Finance: Sources of Finance, Cash Flow & Budgeting",
            desc: "Assessing capital requirements: start-up capital, working capital, and expansion investment. Internal sources (retained profit, asset sales, stock reduction), short-term finance (bank overdraft, trade credit, invoice factoring), and long-term finance (ordinary shares, debentures, bank mortgages, venture capital, angel investors, crowdfunding, Enterprise Ireland/LEO state grants). Differentiating liquidity from profitability, cash-flow forecasting to prevent insolvency, constructing master/functional budgets, and monitoring performance through variance analysis (favourable vs. adverse)."
          },
          {
            title: "International Business: EU, Global Trade & Multinationals",
            desc: "Global trade fundamentals and comparative advantage theory; international trade barriers (tariffs, quotas, regulations, subsidies) and regulatory bodies (WTO, IMF, World Bank). The European Union: institutions (Commission, Parliament, Council), the Single Market (free movement of goods, services, capital, people), Eurozone monetary policy (ECB), Common Agricultural Policy (CAP), and the commercial impact of Brexit on Ireland. Strategic management of Multinational Companies (MNCs): market entry methods (exporting, licensing, franchising, joint ventures, foreign direct investment/subsidiaries), global standardisation vs. local adaptation, and international CSR."
          }
        ]
      },
      {
"""

code = before_biz + new_business + after_biz.split('        id: "accounting",\n')[1]

# 2. Add Curated Topics for Business into CURATED_CONCEPT_TOPICS
curated_business = """      // Business (Irish Leaving Certificate)
      "People in Business & Conflict Resolution": [
        { name: "Stakeholder Ecosystem", cat: "Business Environment", exp: "Analyzing the diverse internal and external stakeholders (owners, employees, customers, suppliers, government, and community) and their interdependence.", items: ["Internal: Owners & Employees", "External: Customers & Suppliers", "Regulatory: Government Agencies", "Social: Local Community Impact"] },
        { name: "Conflicts of Interest", cat: "Organizational Friction", exp: "Examining natural commercial tensions: maximizing shareholder profit vs. fair employee wages, rapid corporate expansion vs. environmental preservation.", items: ["Profit vs. Fair Wages Tension", "Commercial Growth vs. Environment", "Supplier Pricing vs. Cost Reductions", "Customer Value vs. Margin Goals"] },
        { name: "Conflict Resolution", cat: "Negotiation & Law", exp: "Methods to resolve disputes: non-legal negotiation and conciliation, independent third-party mediation, and formal legal adjudication (WRC and Labour Court).", items: ["Direct Bilateral Negotiation", "Third-Party Mediation & Conciliation", "Workplace Relations Commission (WRC)", "Binding Labour Court Rulings"] },
        { name: "Contracts & Trade Unions", cat: "Industrial Relations", exp: "Legally binding employment contracts protecting mutual rights and duties, alongside the protective and bargaining role of trade unions and employer bodies.", items: ["Employment Contract Terms", "Statutory Rights & Employer Duties", "Trade Union Collective Bargaining", "Employer Associations (IBEC)"] }
      ],
      "Management: Motivating, Communicating & Leadership": [
        { name: "Motivation Theories", cat: "Behavioral Management", exp: "Classic motivation frameworks: Maslow's Hierarchy of Needs, Herzberg's Hygiene Factors & Motivators, Taylor's Scientific Management, and Mayo's Human Relations.", items: ["Maslow: Hierarchy of Needs", "Herzberg: Hygiene & Motivators", "Taylor: Scientific Output Pay", "Mayo: Social Human Relations"] },
        { name: "Leadership Styles", cat: "Management Approach", exp: "Contrasting management styles: Autocratic (directive control), Democratic (participative collaboration), Laissez-faire (delegated autonomy), and Situational.", items: ["Autocratic Directive Leadership", "Democratic Participative Style", "Laissez-Faire Delegation", "Situational Adaptive Leadership"] },
        { name: "Business Communication", cat: "Information Flow", exp: "Structuring internal and external communication channels (formal/informal, verbal/written), overcoming barriers (noise, jargon), and leveraging enterprise ICT tools.", items: ["Formal & Informal Channels", "Communication Barrier Removal", "Enterprise ICT & Intranet Systems", "Active Listening & Feedback Loops"] },
        { name: "Change Management", cat: "Organizational Evolution", exp: "Leading organizational transitions: understanding employee resistance to change and applying proactive consultation and support strategies.", items: ["Identifying Sources of Resistance", "Transparent Consultation & Training", "Empowering Change Champions", "Continuous Process Monitoring"] }
      ],
      "Marketing: Market Research & The Marketing Mix": [
        { name: "Market Research Methods", cat: "Market Intelligence", exp: "Synthesizing Primary field research (surveys, interviews, focus groups, observation) and Secondary desk research (CSO census data, industry reports).", items: ["Primary Field Research (Surveys)", "Secondary Desk Research (CSO)", "Sampling Techniques (Random/Stratified)", "Qualitative & Quantitative Insights"] },
        { name: "Product Strategy & Life Cycle", cat: "Product Management", exp: "Managing product portfolios across the 4 Life Cycle stages (Introduction, Growth, Maturity, Decline), differentiation, unique branding, and functional packaging.", items: ["Product Life Cycle (PLC) Stages", "Brand Identity & USP Differentiation", "Protective & Marketing Packaging", "Product Range Diversification"] },
        { name: "Pricing & Distribution (Place)", cat: "Commercial Strategy", exp: "Pricing strategies (penetration, skimming, competitive, psychological) aligned with direct and indirect distribution channels and efficient supply chains.", items: ["Price Skimming & Penetration", "Competitive & Psychological Pricing", "Direct Channels & E-Commerce", "Wholesalers, Retailers & Logistics"] },
        { name: "Promotion & Extended Mix", cat: "Campaign & Services", exp: "Integrated promotional mix (advertising, PR, sales promotions, digital marketing/SEO) and the extended 3 Ps for services (People, Process, Physical Evidence).", items: ["Integrated Advertising & PR", "Digital & Social Media Marketing", "Sales Promotion Incentives", "Extended 3 Ps (People, Process, Evidence)"] }
      ],
      "Domestic Environment: Business, Economy & CSR": [
        { name: "Economic Sectors", cat: "Macro Economy", exp: "Classifying economic activity across Primary (agriculture/mining), Secondary (manufacturing/construction), Tertiary (services), and Quaternary (ICT/R&D).", items: ["Primary (Raw Materials/Farming)", "Secondary (Manufacturing/Assembly)", "Tertiary (Commercial Services)", "Quaternary (ICT & Knowledge/R&D)"] },
        { name: "Business Ownership Structures", cat: "Legal Entities", exp: "Comparing organizational formats: Sole Traders (unlimited liability), Partnerships, Private Limited Companies (Ltd), PLCs, Co-operatives, and Social Enterprises.", items: ["Sole Trader (Personal Control)", "Partnership (Shared Expertise)", "Private Limited Company (Ltd)", "Public Ltd Co (PLC) & Co-operatives"] },
        { name: "Macroeconomic Influences", cat: "Economic Forces", exp: "The operational impact of national economic indicators: inflation rates, interest rate shifts, corporate taxation, unemployment figures, and GDP growth.", items: ["Inflation & Cost Pressures", "Interest Rates & Borrowing Costs", "Taxation & Fiscal Policies", "Economic Growth & Consumer Demand"] },
        { name: "Corporate Social Responsibility", cat: "Business Ethics", exp: "Embedding ethics and sustainability into business operations: environmental preservation, fair trade practices, and positive community investment.", items: ["Ethical Commercial Standards", "Environmental Sustainability", "Fair Trade & Worker Well-Being", "Local Community Investment"] }
      ],
      "Finance: Sources of Finance, Cash Flow & Budgeting": [
        { name: "Sources of Capital", cat: "Financial Planning", exp: "Aligning financial requirements (start-up, working capital, expansion) with internal funds, short-term credit (overdraft/factoring), and long-term equity/debt.", items: ["Internal Funds & Retained Earnings", "Short-Term Overdraft & Trade Credit", "Long-Term Equity & Bank Debt", "Venture Capital & Enterprise Ireland"] },
        { name: "Cash Flow vs. Profitability", cat: "Liquidity Control", exp: "Understanding why profitable companies face insolvency without cash liquidity: forecasting monthly cash inflows and managing debtor collection cycles.", items: ["Accounting Profit vs. Liquid Cash", "Monthly Cash Flow Forecasting", "Accelerating Debtor Payments", "Managing Supplier Credit Terms"] },
        { name: "Budgetary Planning", cat: "Operational Budgets", exp: "Constructing coordinated financial plans: Sales Budgets, Production Budgets, and Cash Budgets consolidated into the Master Corporate Budget.", items: ["Sales Revenue Forecasting", "Production & Material Budgets", "Consolidated Master Budget", "Departmental Resource Allocation"] },
        { name: "Variance Analysis & Control", cat: "Financial Auditing", exp: "Evaluating financial performance by comparing actual figures against budgeted targets, categorizing deviations as Favourable or Adverse.", items: ["Actual vs. Budget Benchmarking", "Favourable Profit Variances", "Adverse Cost Overruns", "Management Corrective Action"] }
      ],
      "International Business: EU, Global Trade & Multinationals": [
        { name: "Global Trade & Advantages", cat: "International Trade", exp: "Why countries trade: theory of comparative advantage, global supply chains, international trade barriers (tariffs/quotas), and WTO oversight.", items: ["Comparative Advantage Theory", "Global Export & Import Dynamics", "Trade Barriers (Tariffs & Quotas)", "World Trade Organization (WTO)"] },
        { name: "The European Union & Ireland", cat: "Single Market & Euro", exp: "The commercial benefits of the EU Single Market (free movement of goods, services, capital, labor), the Eurozone/ECB monetary framework, and Brexit trade impacts.", items: ["EU Single Market (4 Freedoms)", "Eurozone Monetary Policy (ECB)", "Common Agricultural Policy (CAP)", "Brexit Impacts on Irish Trade"] },
        { name: "Multinational Companies (MNCs)", cat: "Global Enterprise", exp: "The role of global enterprises (Apple, Google, Pfizer) in Ireland: job creation, capital investment, technology transfer, and local economic impact.", items: ["Multinational Enterprise Scale", "Foreign Direct Investment (FDI)", "Knowledge & Technology Transfer", "Local Economic Multiplier Effect"] },
        { name: "Market Entry & Global Strategy", cat: "Expansion Methods", exp: "Strategies for entering international markets (exporting, licensing, franchising, joint ventures, subsidiaries) and balancing global standardisation with local adaptation.", items: ["Exporting, Licensing & Franchising", "Joint Ventures & Direct Subsidiaries", "Global Standardisation vs. Adaptation", "International Cultural & Legal Compliance"] }
      ],"""

marker = "    const CURATED_CONCEPT_TOPICS = {\n"
if marker in code:
    code = code.replace(marker, marker + curated_business + "\n")
    print("Injected curated business topics successfully.")
else:
    print("Warning: CURATED_CONCEPT_TOPICS marker not found.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated the_irish_year.html with Business data.")
