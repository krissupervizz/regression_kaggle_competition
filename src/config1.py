ID_COL = ['Id']
REAL_COL = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']
INT_COL = ['MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
 'YearBuilt', 'YearRemodAdd', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF',
 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea',
 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 'GarageArea',
 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch',
 'PoolArea', 'MiscVal', 'MoSold', 'YrSold'] 
OBJ_COL = ['MSZoning', 'Alley', 'LotShape', 'LandContour', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1',
 'Condition2', 'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
 'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating', 'HeatingQC',
 'Electrical', 'KitchenQual', 'Functional', 'FireplaceQu', 'GarageType',
 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive', 'PoolQC', 'Fence', 'MiscFeature',
 'SaleType', 'SaleCondition', 'Street', 'Utilities', 'CentralAir']

OHE_COL = ['Street', 'CentralAir']

ORDER_COL_NAN = ['BsmtQual',
 'BsmtCond', 'GarageQual', 'GarageCond']
ORDER_COL = ['ExterQual','ExterCond', 'HeatingQC', 'KitchenQual']
ORDER_COL_AN = ['BsmtExposure']
ORDER_COL_BSMT = ['BsmtFinType1', 'BsmtFinType2']
ORDER_COL_CARAGE = ['GarageFinish']

CAT_COL = ['MSZoning', 'LotShape', 'LandContour', 'LotConfig', 'LandSlope',
       'Neighborhood', 'Condition1', 'Condition2', 'BldgType',
       'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
       'Exterior2nd', 'MasVnrType', 'Foundation', 'Heating', 'Electrical', 'Functional',
       'GarageType', 'PavedDrive', 'SaleType',
       'SaleCondition', 'Utilities']

TARGET_COL = ['SalePrice']

DROP_COL = ['Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature', 'LotArea', 'BsmtFinSF1', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea', 
            'BedroomAbvGr', 'PoolArea', 'MiscVal', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch']


