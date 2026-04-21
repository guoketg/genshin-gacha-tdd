def calculate_gacha_probability(pull_num):
    if not isinstance(pull_num, int) or pull_num <= 0:
        raise ValueError("抽数必须是正整数")
    
    # 计算实际抽数（超过90抽后重置）
    actual_pull = pull_num % 90
    if actual_pull == 0:
        actual_pull = 90
    
    # 基础概率阶段（1-73抽）
    if 1 <= actual_pull <= 73:
        return 0.006
    # 软保底阶段（74-89抽）
    elif 74 <= actual_pull <= 89:
        return round(0.006 + (actual_pull - 73) * 0.06, 3)
    # 硬保底阶段（第90抽）
    elif actual_pull == 90:
        return 1.0
    else:
        # 理论上不会执行到这里，因为actual_pull的范围是1-90
        return 0.006