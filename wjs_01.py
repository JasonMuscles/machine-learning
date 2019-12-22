from sklearn.feature_extraction import DictVectorizer


def dictvec():
    """字典数据抽取"""
    # 实例化

    dict = DictVectorizer(sparse=False)

    # 调用fit_transfor
    data = dict.fit_transform([{'city': '北京', 'temperature': '100'},
                               {'city': '上海', 'temperature': '60'},
                               {'city': '深圳', 'temperature': '30'}])
    print(data)

    return None


if __name__ == '__main__':
    dictvec()
