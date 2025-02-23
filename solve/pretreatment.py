import numpy as np
import pandas as pd

def str2code(data: pd.DataFrame):
    data = pd.get_dummies(data, columns=['MSZoning'], prefix='Zoning')
    data['Street'] = data['Street'].replace([], [])
    data = pd.get_dummies(data, columns=['Alley'], prefix='Alley')
    data['LotShape'] = data['LotShape'].replace([], [])
    data['LandContour'] = data['LandContour'].replace([], [])
    data['Utilities'] = data['Utilities'].replace([], [])
    data['LotConfig'] = data['LotConfig'].replace([], [])
    data['LandSlope'] = data['LandSlope'].replace([], [])
    data['Neighborhood'] = data['Neighborhood'].replace([], [])
    data['Condition1'] = data['Condition1'].replace([], [])
    data['Condition2'] = data['Condition2'].replace([], [])
    data['BldgType'] = data['BldgType'].replace([], [])
    data['HouseStyle'] = data['HouseStyle'].replace([], [])
    data['RoofStyle'] = data['RoofStyle'].replace([], [])
    data['RoofMatl'] = data['RoofMatl'].replace([], [])
    data['Exterior1st'] = data['Exterior1st'].replace([], [])
    data['Exterior2nd'] = data['Exterior2nd'].replace([], [])
    data['MasVnrType'] = data['MasVnrType'].replace([], [])
    data['ExterQual'] = data['ExterQual'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['ExterCond'] = data['ExterCond'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['Foundation'] = data['Foundation'].replace([], [])
    data['BsmtQual'] = data['BsmtQual'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['BsmtCond'] = data['BsmtCond'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['BsmtExposure'] = data['BsmtExposure'].replace([], [])
    data['BsmtFinType1'] = data['BsmtFinType1'].replace([], [])
    data['BsmtFinType2'] = data['BsmtFinType2'].replace([], [])
    data['Heating'] = data['Heating'].replace([], [])
    data['HeatingQC'] = data['HeatingQC'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['CentralAir'] = data['CentralAir'].replace([], [])
    data['Electrical'] = data['Electrical'].replace([], [])
    data['KitchenQual'] = data['KitchenQual'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['Functional'] = data['Functional'].replace([], [])
    data['FireplaceQu'] = data['FireplaceQu'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['GarageType'] = data['GarageType'].replace([], [])
    data['GarageFinish'] = data['GarageFinish'].replace([], [])
    data['GarageQual'] = data['GarageQual'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['GarageCond'] = data['GarageCond'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['PavedDrive'] = data['PavedDrive'].replace([], [])
    data['PoolQC'] = data['PoolQC'].replace(['Ex','Gd','TA','Fa','Po'], [5,4,3,2,1])
    data['Fence'] = data['Fence'].replace([], [])
    data['MiscFeature'] = data['MiscFeature'].replace([], [])
    data['SaleType'] = data['SaleType'].replace([], [])
    data['SaleCondition'] = data['SaleCondition'].replace([], [])
    return data

def fill_nan(data: pd.DataFrame) -> pd.DataFrame:
    data['LotFrontage'] = data['LotFrontage'].fillna(0)
    data['MasVnrArea'] = data['MasVnrArea'].fillna(0)
    data['BsmtQual']    = data['BsmtQual'].fillna(0)
    data['BsmtCond']    = data['BsmtCond'].fillna(0)

    data['BsmtFinSF1'] = data['BsmtFinSF1'].fillna(0)
    data['BsmtFinSF2'] = data['BsmtFinSF2'].fillna(0)
    data['BsmtUnfSF'] = data['BsmtUnfSF'].fillna(0)
    data['TotalBsmtSF'] = data['TotalBsmtSF'].fillna(0)

    data['BsmtFullBath'] = data['BsmtFullBath'].fillna(0)
    data['BsmtHalfBath'] = data['BsmtHalfBath'].fillna(0)

    data['KitchenQual'] = data['KitchenQual'].fillna(0)

    data['ExistFireplace'] = 1
    data.loc[data['FireplaceQu'].isna(), 'ExistFireplace'] = 0
    data['FireplaceQu'] = data['FireplaceQu'].fillna(0)

    data['ExistGarage'] = 1
    data.loc[data['GarageYrBlt'].isna(), 'ExistGarage'] = 0
    data['GarageYrBlt'] = data['GarageYrBlt'].fillna(0)
    data['GarageCars'] = data['GarageCars'].fillna(0)
    data['GarageArea'] = data['GarageArea'].fillna(0)
    data['GarageQual'] = data['GarageQual'].fillna(0)
    data['GarageCond'] = data['GarageCond'].fillna(0)

    data['ExistPool'] = 1
    data.loc[data['PoolQC'].isna(), 'ExistPool'] = 0
    data['PoolQC'] = data['PoolQC'].fillna(0)

    return data

def drop_str(data: pd.DataFrame) -> pd.DataFrame:
    return data.select_dtypes(exclude=['object'])