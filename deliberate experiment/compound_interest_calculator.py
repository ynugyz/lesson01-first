# 复利计算器（交互式）
# 公式：A = P * (1 + r/n)^(n*t)
#   A = 最终本息和
#   P = 本金
#   r = 年利率（小数）
#   n = 每年复利次数
#   t = 存款年数


def get_number(prompt, default=None):
    """读取一个数字，输入为空时使用 default。"""
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            return float(raw)
        except ValueError:
            print("  输入无效，请重新输入一个数字。")


def compound_interest(P, r, n, t):
    """按复利公式计算最终本息和。"""
    return P * (1 + r / n) ** (n * t)


def print_yearly_table(P, r, n, t):
    """打印逐年本息和明细表。"""
    period_rate = r / n
    print("\n逐年明细（年末本息和）：")
    print(f"{'年份':>6} | {'期末本息和':>14} | {'累计利息':>14}")
    print("-" * 42)
    balance = P
    for year in range(1, int(t) + 1):
        balance = P * (1 + period_rate) ** (n * year)
        interest = balance - P
        print(f"{year:>6} | {balance:>14.2f} | {interest:>14.2f}")
    print("-" * 42)


def main():
    print("=" * 42)
    print("       复利计算器（交互式）")
    print("=" * 42)

    P = get_number("请输入本金 P（元，默认 10000）：", default=10000)
    r = get_number("请输入年利率 r（%，默认 5）：", default=5) / 100
    n = int(get_number(
        "请输入每年复利次数 n（1=年，2=半年，4=季，12=月，365=日，默认 1）：",
        default=1,
    ))
    t = get_number("请输入存期 t（年，默认 3）：", default=3)

    A = compound_interest(P, r, n, t)
    interest = A - P

    print("\n计算结果：")
    print(f"  本金：{P:.2f} 元")
    print(f"  年利率：{r * 100:.2f}%")
    print(f"  每年复利次数：{n}")
    print(f"  存期：{t:.0f} 年")
    print(f"  最终本息和：{A:.2f} 元")
    print(f"  累计利息：{interest:.2f} 元")

    print_yearly_table(P, r, n, t)


if __name__ == "__main__":
    main()
