"""
代码优化示例 - Python 版本
演示常见的优化模式，包含 before/after 对比和基准测试
"""

import time
from functools import lru_cache


def benchmark(func, *args, iterations=1000):
    """简单基准测试工具"""
    start = time.perf_counter()
    for _ in range(iterations):
        result = func(*args)
    elapsed = time.perf_counter() - start
    return elapsed, result


# =============================================================================
# 示例 1: 查找优化 - 列表 vs 集合
# =============================================================================

def find_duplicates_slow(data):
    """O(n²) - 嵌套循环查找重复"""
    duplicates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    return duplicates


def find_duplicates_fast(data):
    """O(n) - 使用集合查找重复"""
    seen = set()
    duplicates = set()
    for item in data:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)


# =============================================================================
# 示例 2: 字符串拼接优化
# =============================================================================

def concat_slow(items):
    """使用 += 拼接字符串 - 每次创建新对象"""
    result = ""
    for item in items:
        result += str(item) + ", "
    return result.rstrip(", ")


def concat_fast(items):
    """使用 join - 一次性拼接"""
    return ", ".join(str(item) for item in items)


# =============================================================================
# 示例 3: 缓存优化 - 递归计算
# =============================================================================

def fibonacci_slow(n):
    """无缓存 - O(2^n) 指数复杂度"""
    if n < 2:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


@lru_cache(maxsize=None)
def fibonacci_fast(n):
    """带缓存 - O(n) 线性复杂度"""
    if n < 2:
        return n
    return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)


# =============================================================================
# 示例 4: 字典构建优化
# =============================================================================

def build_index_slow(records):
    """逐条检查并构建索引"""
    index = {}
    for record in records:
        key = record["category"]
        if key not in index:
            index[key] = []
        index[key].append(record)
    return index


def build_index_fast(records):
    """使用 defaultdict 构建索引"""
    from collections import defaultdict
    index = defaultdict(list)
    for record in records:
        index[record["category"]].append(record)
    return dict(index)


# =============================================================================
# 示例 5: 批量处理 vs 逐条处理
# =============================================================================

def process_one_by_one(data, batch_processor):
    """逐条处理"""
    results = []
    for item in data:
        results.append(batch_processor([item])[0])
    return results


def process_in_batches(data, batch_processor, batch_size=100):
    """批量处理"""
    results = []
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        results.extend(batch_processor(batch))
    return results


# =============================================================================
# 运行基准测试
# =============================================================================

if __name__ == "__main__":
    import random

    print("=" * 60)
    print("代码优化基准测试")
    print("=" * 60)

    # 测试 1: 查找重复
    data = [random.randint(0, 500) for _ in range(1000)]
    t_slow, _ = benchmark(find_duplicates_slow, data, iterations=10)
    t_fast, _ = benchmark(find_duplicates_fast, data, iterations=10)
    print(f"\n[查找重复] 列表搜索: {t_slow:.4f}s  |  集合搜索: {t_fast:.4f}s  |  加速: {t_slow/t_fast:.1f}x")

    # 测试 2: 字符串拼接
    items = list(range(10000))
    t_slow, _ = benchmark(concat_slow, items, iterations=100)
    t_fast, _ = benchmark(concat_fast, items, iterations=100)
    print(f"[字符串拼接] += 拼接: {t_slow:.4f}s  |  join 拼接: {t_fast:.4f}s  |  加速: {t_slow/t_fast:.1f}x")

    # 测试 3: 斐波那契
    t_slow, _ = benchmark(fibonacci_slow, 30, iterations=1)
    t_fast, _ = benchmark(fibonacci_fast, 30, iterations=1)
    print(f"[斐波那契]  无缓存: {t_slow:.4f}s  |  lru_cache: {t_fast:.6f}s  |  加速: {t_slow/t_fast:.0f}x")

    # 测试 4: 字典构建
    records = [{"category": f"cat_{random.randint(0, 50)}", "value": i} for i in range(10000)]
    t_slow, _ = benchmark(build_index_slow, records, iterations=100)
    t_fast, _ = benchmark(build_index_fast, records, iterations=100)
    print(f"[字典构建]  手动检查: {t_slow:.4f}s  |  defaultdict: {t_fast:.4f}s  |  加速: {t_slow/t_fast:.1f}x")

    print("\n" + "=" * 60)
    print("测试完成")
