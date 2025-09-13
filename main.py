__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import argparse
from proposal_crew.crew import run_proposal_crew

parser = argparse.ArgumentParser(description="Generate an AI proposal for a given company.")
parser.add_argument("company", type=str, help="The name of the company or industry to research.")
args = parser.parse_args()
company_name = args.company

if __name__ == '__main__':
    print(f"🚀 Crew: Kicking off the full analysis and proposal generation for {company_name}...")
    
    # Run the crew and get the result
    result = run_proposal_crew(company_name)
    
    print("\n\n########################")
    print("## Here is the Final Proposal: \n")
    print(result)

    file_name = f"{company_name.replace(' ', '_').lower()}_ai_proposal.md"
    with open(file_name, "w") as f:
        f.write(result)
    print(f"\n\n✅ Final proposal has been saved to {file_name}")