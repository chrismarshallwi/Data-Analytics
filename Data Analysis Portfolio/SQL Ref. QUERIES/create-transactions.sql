--Creating the table given that it does not exist
IF Object_ID('sandboxtest') IS NULL

CREATE TABLE [sandbox].[dbo].[sandboxtest]
(
    [Branch_Name] VARCHAR(15) NOT NULL,
    [Account_Deposit_Category_Desc] INTEGER NOT NULL,
    [Txn_Amount] INTEGER NOT NULL,
    [Txn_Total_Number_of_Transactions] INTEGER NOT NULL,
);