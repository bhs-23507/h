import sqlite3

DATABASE = "company.db"

def print_all_companies():
    "print all companies"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"company name                  market cap          foun.year    foun.name             sector")
    for company in results:
        print(f"{company[1]:<30}{company[2]:<20}{company[3]:<13}{company[4]:<22}{company[5]:<10}")
    db.close()

def print_all_info_of_first_company():
    "print all information on first company"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company WHERE id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"company name                 market cap          foun.year    foun.name             sector")
    for company in results:
        print(f"{company[1]:<30}{company[2]:<20}{company[3]:<10}{company[4]:<22}{company[5]:<10}")
    db.close()

def print_all_info_of_top_three_companies():
    "print all information of the top three companies"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company WHERE id < '4';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"company name                 market cap          foun.year    foun.name             sector")
    for company in results:
        print(f"{company[1]:<30}{company[2]:<20}{company[3]:<10}{company[4]:<22}{company[5]:<10}")
    db.close()

def print_all_companies_sorted_by_founding_year():
    "print all companies sorted by founding year"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company ORDER BY founding_year DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"company name                 market cap          foun.year    foun.name             sector")
    for company in results:
        print(f"{company[1]:<30}{company[2]:<20}{company[3]:<10}{company[4]:<22}{company[5]:<10}")
    db.close()

def print_all_companies_with_sector_Technology():
    "print all companies with the sector Technology"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company WHERE sector = 'Technology';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"company name                 market cap          foun.year    foun.name             sector")
    for company in results:
        print(f"{company[1]:<30}{company[2]:<20}{company[3]:<10}{company[4]:<22}{company[5]:<10}")
    db.close()

def print_all_companies_sorted_by_market_cap():
    "print all companies sorted by market cap"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company ORDER BY market_cap DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"company name                 market cap          foun.year    foun.name             sector")
    for company in results:
        print(f"{company[1]:<30}{company[2]:<20}{company[3]:<10}{company[4]:<22}{company[5]:<10}")
    db.close()

def print_all_info_of_top_five_companies():
    "print all information of the top five companies"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company WHERE id <= '5';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"company name                 market cap          foun.year    foun.name             sector")
    for company in results:
        print(f"{company[1]:<30}{company[2]:<20}{company[3]:<10}{company[4]:<22}{company[5]:<10}")
    db.close()

def print_all_companies_with_market_cap_more_than_trillion():
    "print all companies with more than a trllion, market cap"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company WHERE market_cap > 1000000000000;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"company name                 market cap          foun.year    foun.name             sector")
    for company in results:
        print(f"{company[1]:<30}{company[2]:<20}{company[3]:<10}{company[4]:<22}{company[5]:<10}")
    db.close()

while True:
    user_input = input("1. Print all companies\n2. Print all information of the first company\n3. Print all information of the top three companies\n4. Print all companies sorted by founding year\n5. Print all companies with the sector Technology\n6. Print all companies sorted by market cap\n7. Print all information of the top five companies\n8. Print all companies with market cap more than a trillion\n9. Exit\n")
    if user_input == "1":
        print_all_companies()
    elif user_input == "2":
        print_all_info_of_first_company()
    elif user_input == "3":
        print_all_info_of_top_three_companies()
    elif user_input == "4":
        print_all_companies_sorted_by_founding_year()
    elif user_input == "5":
        print_all_companies_with_sector_Technology()
    elif user_input == "6":
        print_all_companies_sorted_by_market_cap()
    elif user_input == "7":
        print_all_info_of_top_five_companies()
    elif user_input == "8":
        print_all_companies_with_market_cap_more_than_trillion()
    elif user_input == "9":
        break
    else:
        print("That was not an option\n")