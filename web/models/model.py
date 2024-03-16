import pickle
import gzip
import pandas as pd

def model_pred(dict_data):
    # 模型載入
    with gzip.open('../model/xgboost-fruitprice.pgz', 'r') as f:
      regressor_op = pickle.load(f)

    # 整理要導入模型的DATAFRAME
    zero_list = [0] * 42
    X_df = pd.DataFrame([zero_list], 
    columns=['811', '812', 'tp', 'rt_T_F', 'wd', 'fs', 'lu_dt_fs', 'br', 'total_nw', 'all_total_nw',
              '008', '018', '032', '039', '049', '051', '059', '061', '063', '066', '068', '069', '083', '096', '099', '107', '108', '595', '707', '716',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    X_df['tp'] = X_df['tp'].astype(float)
    X_df['total_nw'] = X_df['total_nw'].astype(float)
    X_df['all_total_nw'] = X_df['all_total_nw'].astype(float)

    X_df[dict_data["fruit"]] = 1

    X_df["tp"] = float(dict_data["temp"])

    if dict_data["rain"] == "T":
      X_df["rt_T_F"] = 1
    else:
      X_df["rt_T_F"] = 0

    keys = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    values = [6, 0, 1, 2, 3, 4, 5] #模型的星期一值為0
    week_dict = dict(zip(keys, values))
    X_df["wd"] = week_dict[dict_data["week"]]

    if dict_data["festival"] == "YES":
       X_df["fs"] = 1
    else:
       X_df["fs"] = 0

    if dict_data["lu_festival"] == "YES":
       X_df["lu_dt_fs"] = 1
    else:
       X_df["lu_dt_fs"] = 0

    X_df['br'] = int(dict_data["people_num"])
    X_df['total_nw'] = float(dict_data["weight"])
    X_df['all_total_nw'] = float(dict_data["total_weight"])
    X_df[dict_data["sales"]] = 1
    X_df[dict_data["month"]] = 1

    #導入模型輸出結果
    result = regressor_op.predict(X_df)[0]
    return result

# ==================測試用 ===================================
# with gzip.open('../model/xgboost-fruitprice.pgz', 'r') as f:
#     regressor_op = pickle.load(f)

# X_test = pd.DataFrame([[0, 1, 25, 0, 3, 0, 0, 40, 3000, 10000, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]], 
# columns=['811', '812', 'tp', 'rt_T_F', 'wd', 'fs', 'lu_dt_fs', 'br', 'total_nw', 'all_total_nw',
#           '008', '018', '032', '039', '049', '051', '059', '061', '063', '066', '068', '069', '083', '096', '099', '107', '108', '595', '707', '716',
#             '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
# print(X_test.head())
# pred_test = regressor_op.predict(X_test)
# print(pred_test[:])