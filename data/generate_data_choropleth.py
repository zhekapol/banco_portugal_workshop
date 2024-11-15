import pandas as pd
import numpy as np

# Provided IDs
ids = np.array(['0101', '0102', '0103', '0104', '0105', '0106', '0107', '0108', '0109', '0110', 
                '0111', '0112', '0113', '0114', '0115', '0116', '0117', '0118', '0119', '0201',
                '0202', '0203', '0204', '0205', '0206', '0207', '0208', '0209', '0210', '0211',
                '0212', '0213', '0214', '0301', '0302', '0303', '0304', '0305', '0306', '0307',
                '0308', '0309', '0310', '0311', '0312', '0313', '0314', '0401', '0402', '0403',
                '0404', '0405', '0406', '0407', '0408', '0409', '0410', '0411', '0412', '0501',
                '0502', '0503', '0504', '0505', '0506', '0507', '0508', '0509', '0510', '0511',
                '0601', '0602', '0603', '0604', '0605', '0606', '0607', '0608', '0609', '0610',
                '0611', '0612', '0613', '0614', '0615', '0616', '0617', '0701', '0702', '0703',
                '0704', '0705', '0706', '0707', '0708', '0709', '0710', '0711', '0712', '0713',
                '0714', '0801', '0802', '0803', '0804', '0805', '0806', '0807', '0808', '0809',
                '0810', '0811', '0812', '0813', '0814', '0815', '0816', '0901', '0902', '0903',
                '0904', '0905', '0906', '0907', '0908', '0909', '0910', '0911', '0912', '0913',
                '0914', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009',
                '1010', '1011', '1012', '1013', '1014', '1015', '1016', '1101', '1102', '1103',
                '1104', '1105', '1106', '1107', '1108', '1109', '1110', '1111', '1112', '1113',
                '1114', '1115', '1116', '1201', '1202', '1203', '1204', '1205', '1206', '1207',
                '1208', '1209', '1210', '1211', '1212', '1213', '1214', '1215', '1301', '1302',
                '1303', '1304', '1305', '1306', '1307', '1308', '1309', '1310', '1311', '1312',
                '1313', '1314', '1315', '1316', '1317', '1318', '1401', '1402', '1403', '1404',
                '1405', '1406', '1407', '1408', '1409', '1410', '1411', '1412', '1413', '1414',
                '1415', '1416', '1417', '1418', '1419', '1420', '1421', '1501', '1502', '1503',
                '1504', '1505', '1506', '1507', '1508', '1509', '1510', '1511', '1512', '1513',
                '1601', '1602', '1603', '1604', '1605', '1606', '1607', '1608', '1609', '1610',
                '1701', '1702', '1703', '1704', '1705', '1706', '1707', '1708', '1709', '1710',
                '1711', '1712', '1713', '1714', '1801', '1802', '1803', '1804', '1805', '1806',
                '1807', '1808', '1809', '1810', '1811', '1812', '1813', '1814', '1815', '1816',
                '1817', '1818', '1819', '1820', '1821', '1822', '1823', '1824', '3101', '3102',
                '3103', '3104', '3105', '3106', '3107', '3108', '3109', '3110', '3201', '4101',
                '4201', '4202', '4203', '4204', '4205', '4206', '4301', '4302', '4401', '4501',
                '4502', '4601', '4602', '4603', '4701', '4801', '4802', '4901'])

# Random buying power values (between 1000 and 10000)
buying_power = np.random.uniform(1000, 10000, size=len(ids))

# Randomly assigned categories
categories = np.random.choice(['Low', 'Medium', 'High'], size=len(ids))

# Create DataFrame
data = pd.DataFrame({
    'c_mun': ids,
    'Buying_Power': buying_power,
    'Relevance': categories
})

# Display the first few rows of the data
print(data.head())

data.to_csv("data_choropleth.csv")
