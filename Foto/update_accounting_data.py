# Script to update Accounting in IRELAND_SUBJECTS and CURATED_CONCEPT_TOPICS with exact text from docx
import re

html_path = r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html'
with open(html_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Accounting in IRELAND_SUBJECTS
old_accounting = """      {
        id: "accounting",
        name: "Accounting",
        type: "Finance",
        image: IMAGES.subjects.accounting,
        summary: "Hands-on financial accounting: ledger management, cash flow statements, balance sheet interpretation, and cost management.",
        keywords: ["Balance Sheet", "Cash Flow", "Cost Control", "Financial Management"],
        topics: ["Financial Accounting", "Club & Service A/C's", "Cashflow Statements", "Bank Reconciliation", "Management Accounting & Budgets"],
        reflection: "Developing a financial mindset: reading balance sheets, mitigating risk, and auditing yearly performance.",
        detailedTopics: [
          {
            title: "Financial Accounting & Double-Entry Principles",
            desc: "Rigorous application of the double-entry bookkeeping system, balancing ledger accounts, managing debtors/creditors, recording depreciations, prepayments, and accruals."
          },
          {
            title: "Club & Service Organization Accounts",
            desc: "Preparing receipts and payments accounts, accumulated funds, and income/expenditure statements for non-profit entities, sports clubs, and service firms."
          },
          {
            title: "Cash Flow Statements & Liquidity Analysis",
            desc: "Constructing cash flow statements to monitor real-time liquidity, differentiating between operating profitability and cash solvency to avert insolvency crises."
          },
          {
            title: "Bank Reconciliation Statements",
            desc: "Auditing internal cash books against monthly bank statements to detect unpresented cheques, direct debits, standing orders, and banking discrepancies."
          },
          {
            title: "Management Accounting & Budgetary Control",
            desc: "Marginal costing, calculating the Break-Even Point (BEP), analyzing fixed vs. variable cost structures, and producing projected master budgets for strategic executive decision-making."
          }
        ]
      },"""

new_accounting = """      {
        id: "accounting",
        name: "Accounting",
        type: "Finance",
        image: IMAGES.subjects.accounting,
        summary: "Systematic recording and reporting of enterprise financial operations: double-entry bookkeeping, cash flow solvency, internal budgetary control, non-profit club accounts, and bank reconciliation.",
        keywords: ["Double-Entry", "Cash Flow", "Budgetary Control", "Bank Reconciliation"],
        topics: [
          "Financial Accounting & Double-Entry Principles",
          "Cash Flow Statement & Liquidity Analysis",
          "Management Accounting & Budgetary Control",
          "Club, Service Firm & Organisation Accounts",
          "Bank Reconciliation Statement"
        ],
        reflection: "Developing financial mastery: applying double-entry rigor, auditing cash flow solvency, controlling corporate budgets, and resolving banking discrepancies.",
        detailedTopics: [
          {
            title: "Financial Accounting & Double-Entry Principles",
            desc: "Financial accounting systematically records and reports an enterprise's economic and financial transactions for external stakeholders (investors, banks, suppliers, and tax authorities). It is governed by the core Accounting Equation (Assets = Liabilities + Equity) and the Double-Entry system, where every transaction affects at least two accounts with total Debits (Dr) equaling total Credits (Cr). The accounting cycle advances through the Journal (chronological recording), General Ledger (posting to individual accounts), Trial Balance (arithmetic debit-credit verification), and final Financial Statements."
          },
          {
            title: "Cash Flow Statement & Liquidity Analysis",
            desc: "The Cash Flow Statement tracks actual gross inflows and outflows of cash over a reporting period, establishing a crucial distinction between accounting profit and real cash solvency. Cash flows are classified into Operating Activities (core customer receipts, supplier and employee payments), Investing Activities (purchase/sale of equipment, property, and investments), and Financing Activities (bank loans, share issuance, debt repayments, and dividends). Key liquidity metrics include the Current Ratio (Current Assets / Current Liabilities), Quick Ratio ((Current Assets - Inventory) / Current Liabilities), and Cash Ratio (Cash / Current Liabilities), supported by proactive strategies to manage receivables, inventory, and supplier payment terms."
          },
          {
            title: "Management Accounting & Budgetary Control",
            desc: "Management accounting produces forward-looking financial intelligence tailored for internal managers to plan strategic operations, allocate resources, and monitor departmental performance. Unlike financial accounting, it is unrestricted by mandatory statutory templates. It establishes comprehensive Master Budgets synthesizing Sales Budgets, Production Budgets, and Cash Budgets. Budgetary control continuously benchmarks actual outcomes against planned figures through Variance Analysis, isolating deviations as Favourable (enhancing profitability) or Adverse (eroding financial performance)."
          },
          {
            title: "Club, Service Firm & Organisation Accounts",
            desc: "Accounting methodologies structured across distinct enterprise types. For non-profit clubs and societies aimed at member service rather than profit distribution, annual performance yields a Surplus or Deficit via Receipts and Payments Accounts (cash flows) and Income and Expenditure Accounts (accruals-based), with net worth recorded in the Accumulated Fund alongside Subscriptions in Arrears (assets), Subscriptions in Advance (liabilities), and Life Memberships. For service firms, net profit derives from service revenues minus direct and operating expenses, while organizational frameworks contrast Sole Traders (capital and personal drawings), Partnerships (profit-sharing appropriation accounts), and Limited Companies (share capital and retained reserves)."
          },
          {
            title: "Bank Reconciliation Statement",
            desc: "The Bank Reconciliation Statement systematically audits and explains discrepancies between the enterprise's internal Cash Book balance and the official Bank Statement balance. It identifies timing differences and unrecorded items, including unpresented cheques (issued by the firm but not yet cleared by the bank), outstanding lodgements (funds deposited but not yet credited), bank charges, standing orders, direct debits, interest transactions, and dishonoured cheques. The standardized audit procedure updates the internal Cash Book first before compiling the reconciliation statement to balance both records."
          }
        ]
      },"""

if old_accounting in code:
    code = code.replace(old_accounting, new_accounting)
    print("Replaced Accounting in IRELAND_SUBJECTS successfully.")
else:
    print("Warning: old_accounting exact match not found.")

# 2. Add English Accounting Topics to CURATED_CONCEPT_TOPICS
accounting_curated_topics = """      // Accounting (Irish Leaving Certificate)
      "Financial Accounting & Double-Entry Principles": [
        { name: "The Accounting Equation", cat: "Fundamental Theory", exp: "Assets = Liabilities + Equity. The fundamental foundation ensuring that all enterprise resources are perfectly funded by external debt or internal equity capital.", items: ["Assets (Enterprise Resources)", "Liabilities (External Obligations)", "Equity (Capital & Retained Earnings)", "Continuous Systemic Equilibrium"] },
        { name: "Double-Entry Bookkeeping", cat: "Recording Mechanics", exp: "Every financial transaction affects at least two accounts with total Debits (Dr) equaling total Credits (Cr). Assets and Expenses increase on Debit, while Liabilities, Equity, and Revenue increase on Credit.", items: ["Debit (Dr) = Inflow of Value / Cost", "Credit (Cr) = Outflow of Value / Source", "T-Account Ledger Posting", "Arithmetic Error Detection"] },
        { name: "Accounting Cycle Stages", cat: "Operational Workflow", exp: "The structured four-stage accounting sequence: Journal (chronological transaction entry), Ledger (account categorization), Trial Balance (arithmetic audit), and Financial Statements.", items: ["Journal (Chronological Log)", "General Ledger (T-Accounts)", "Trial Balance (Debit-Credit Check)", "Financial Statements (Balance Sheet)"] },
        { name: "Transaction Verification", cat: "Auditing & Control", exp: "Practical execution of double-entry rules (e.g. purchasing raw materials for cash results in Dr Purchases, Cr Cash), ensuring a rigorous and verifiable audit trail.", items: ["Source Document Validation", "Dr Purchases / Cr Cash Entry", "Accruals & Prepayments Adjustment", "Closing Balances Computation"] }
      ],
      "Cash Flow Statement & Liquidity Analysis": [
        { name: "Cash Flow vs. Profit", cat: "Solvency Analysis", exp: "A profitable firm can face bankruptcy if cash inflows are insufficient to settle immediate short-term obligations. Cash flow measures tangible liquidity rather than accounting profit.", items: ["Accrual Profit vs. Real Cash", "Insolvency Risk Prevention", "Working Capital Timing", "Liquidity Buffer Maintenance"] },
        { name: "Three Flow Categories", cat: "Cash Flow Structure", exp: "Segregating cash flows into Operating Activities (customer receipts, supplier/wage payments), Investing Activities (fixed asset purchases/sales), and Financing Activities (loans, share capital, dividends).", items: ["Operating Activities (Core Business)", "Investing Activities (Capital Expenditure)", "Financing Activities (Debt & Equity)", "Net Change in Cash Position"] },
        { name: "Liquidity Ratios", cat: "Financial Metrics", exp: "Key metrics assessing short-term solvency: Current Ratio (CA/CL), Quick/Acid-Test Ratio ((CA-Inventory)/CL), and Cash Ratio (Cash/CL).", items: ["Current Ratio (CA / CL)", "Quick Ratio ((CA - Inventory) / CL)", "Cash Ratio (Cash / CL)", "Solvency Benchmark Evaluation"] },
        { name: "Working Capital Management", cat: "Liquidity Strategy", exp: "Proactive cash optimization: accelerating debtor collections, minimizing slow-moving stock holding, negotiating supplier trade credit terms, and utilizing short-term credit facilities.", items: ["Accelerating Debtor Receipts", "Inventory Cycle Optimization", "Supplier Credit Negotiation", "Short-Term Credit & Factoring"] }
      ],
      "Management Accounting & Budgetary Control": [
        { name: "Internal Managerial Focus", cat: "Decision Support", exp: "Internal reporting tailored for executive decision-makers, emphasizing future forecasts, departmental efficiency, and resource allocation without statutory format restrictions.", items: ["Internal Executive Audience", "Future Planning Orientation", "Unrestricted Flexible Formats", "Departmental & Product Granularity"] },
        { name: "Master & Functional Budgets", cat: "Budget Architecture", exp: "Coordinated budget preparation: Sales Budget (revenue forecasts), Production Budget (manufacturing volume), and Cash Budget (monthly inflow/outflow projections), united into the Master Budget.", items: ["Sales Budget (Volume & Revenue)", "Production Budget (Material/Labour)", "Cash Budget (Monthly Liquidity)", "Master Budget (Consolidated Plan)"] },
        { name: "Budgetary Control", cat: "Performance Monitoring", exp: "Continuous comparison between planned budget targets and actual operational performance, enabling management by exception and rapid corrective intervention.", items: ["Target Setting & Allocation", "Actual Performance Tracking", "Benchmarking & Deviation Flagging", "Management by Exception"] },
        { name: "Variance Analysis", cat: "Cost Control", exp: "Quantifying variances between budget and actual results: classified as Favourable (improving net profit) or Adverse (increasing costs or reducing revenue).", items: ["Variance Identification (Actual vs. Budget)", "Favourable Variances (Profit Boost)", "Adverse Variances (Cost Overruns)", "Root Cause Corrective Actions"] }
      ],
      "Club, Service Firm & Organisation Accounts": [
        { name: "Non-Profit Club Accounts", cat: "Non-Profit Sector", exp: "Accounting for sports clubs and societies focused on member service: annual outcomes yield a Surplus or Deficit, recorded in the Accumulated Fund rather than equity capital.", items: ["Receipts & Payments Account (Cash)", "Income & Expenditure Account (Accruals)", "Accumulated Fund (Club Net Worth)", "Annual Surplus or Deficit"] },
        { name: "Subscription Accounting", cat: "Membership Revenue", exp: "Managing club membership revenue: Subscriptions in Arrears (uncollected fees = Assets), Subscriptions in Advance (prepaid fees = Liabilities), and Life Memberships (treated as capital fund).", items: ["Subscriptions in Arrears (Current Asset)", "Subscriptions in Advance (Current Liability)", "Life Membership (Capital Reserve)", "Annual Revenue Recognition"] },
        { name: "Service Firm Accounts", cat: "Service Industry", exp: "Financial reporting for service providers (hotels, consultancies, practices) where revenue derives from professional fees minus direct labor and operating overheads.", items: ["Fee Revenue Recognition", "Direct Labour & Project Costs", "Operating Overheads Allocation", "Net Service Profitability"] },
        { name: "Organisation Structures", cat: "Legal Formats", exp: "Contrasting organizational accounts: Sole Traders (single capital & drawings), Partnerships (profit-sharing appropriation accounts), and Limited Companies (share capital & retained earnings).", items: ["Sole Trader (Capital & Drawings)", "Partnership (Appropriation Accounts)", "Limited Company (Share Capital)", "Retained Earnings Reserves"] }
      ],
      "Bank Reconciliation Statement": [
        { name: "Reconciliation Objective", cat: "Audit & Verification", exp: "Systematic procedure matching the internal Cash Book balance against the external Bank Statement balance to explain timing differences and detect errors.", items: ["Cash Book vs. Bank Statement", "Timing Discrepancies Resolution", "Omission Error Correction", "Internal Control & Fraud Prevention"] },
        { name: "Timing Differences", cat: "Discrepancy Sources", exp: "Explaining timing variances: unpresented cheques (issued but not yet presented for payment), outstanding lodgements (deposited but not yet credited), and dishonoured cheques.", items: ["Unpresented Cheques (Issued to Payees)", "Outstanding Lodgements (Deposits in Transit)", "Dishonoured Cheques (Failed Clearance)", "Bank Clearing Timelines"] },
        { name: "Direct Bank Entries", cat: "Automated Banking", exp: "Transactions initiated directly by the bank that must be posted to the Cash Book: bank service charges, interest earned/charged, standing orders, and direct debits.", items: ["Bank Charges & Fees", "Direct Debits & Standing Orders", "Credit Transfers & Dividends", "Accrued Bank Interest"] },
        { name: "Standard Audit Procedure", cat: "Reconciliation Process", exp: "Step 1: Update the Cash Book with missing bank entries. Step 2: Compare entries and isolate residual differences. Step 3: Draft the Bank Reconciliation Statement to balance both records.", items: ["Cash Book Updating (First Step)", "Adjusted Cash Book Balance", "Bank Statement Reconciliation", "Final Arithmetic Alignment"] }
      ],"""

marker = "    const CURATED_CONCEPT_TOPICS = {\n      // Storia"
if marker in code:
    code = code.replace(marker, "    const CURATED_CONCEPT_TOPICS = {\n" + accounting_curated_topics + "\n      // Storia")
    print("Injected Accounting into CURATED_CONCEPT_TOPICS successfully.")
else:
    print("Warning: CURATED_CONCEPT_TOPICS marker not found.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated the_irish_year.html.")
