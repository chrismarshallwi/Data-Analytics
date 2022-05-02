SELECT Branch_Name, Account_Deposit_Category_Desc, 
ROUND(SUM(Txn_Amount),2) AS Sum_Txn_Amount, 
ROUND(AVG(Txn_Amount),2) AS Avg_Txn_Amount, 
SUM(Txn_Total_Number_of_Transactions) AS Total_Txns
FROM transactions
WHERE Branch_Name IS NOT NULL AND Account_Deposit_Category_Desc IS NOT NULL AND Account_Deposit_Category_Desc != 'Revolving Credit'
GROUP BY Branch_Name, Account_Deposit_Category_Desc
ORDER BY Branch_Name, Avg_Txn_Amount DESC