# 代码优化分析 Playbook

## 概述

本 Playbook 提供系统性的代码优化分析框架，涵盖性能优化、内存优化、可读性优化和架构优化四个核心维度。

---

## 1. 性能优化

### 1.1 算法复杂度优化

| 优化类型 | 优化前 | 优化后 | 提升幅度 |
|---------|--------|--------|---------|
| 查找操作 | O(n) 线性搜索 | O(1) 哈希表查找 | ~100x (n=1000) |
| 排序操作 | O(n²) 冒泡排序 | O(n log n) 快排 | ~10x (n=1000) |
| 去重操作 | O(n²) 嵌套循环 | O(n) Set 去重 | ~100x (n=1000) |

### 1.2 循环优化

**避免在循环内重复计算：**

```python
# 优化前 - 每次循环都计算 len()
for i in range(len(data)):
    if data[i] > threshold:
        results.append(data[i])

# 优化后 - 使用列表推导式
results = [x for x in data if x > threshold]
```

**减少循环嵌套层数：**

```python
# 优化前 - O(n*m) 嵌套查找
def find_common(list_a, list_b):
    common = []
    for a in list_a:
        for b in list_b:
            if a == b:
                common.append(a)
    return common

# 优化后 - O(n+m) 集合交集
def find_common(list_a, list_b):
    return list(set(list_a) & set(list_b))
```

### 1.3 I/O 优化

```python
# 优化前 - 逐行写入文件
for line in lines:
    with open("output.txt", "a") as f:
        f.write(line + "\n")

# 优化后 - 批量写入
with open("output.txt", "w") as f:
    f.write("\n".join(lines))
```

---

## 2. 内存优化

### 2.1 生成器替代列表

```python
# 优化前 - 一次性加载所有数据到内存
def read_large_file(path):
    lines = []
    with open(path) as f:
        for line in f:
            lines.append(line.strip())
    return lines

# 优化后 - 使用生成器按需加载
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
```

### 2.2 使用 `__slots__` 减少对象内存

```python
# 优化前 - 默认 __dict__ 存储属性
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 优化后 - 使用 __slots__，内存减少约 40%
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### 2.3 及时释放引用

```python
# 优化前 - 大对象长期占用内存
def process():
    large_data = load_huge_dataset()
    summary = compute_summary(large_data)
    # large_data 仍在内存中
    return format_report(summary)

# 优化后 - 及时释放
def process():
    large_data = load_huge_dataset()
    summary = compute_summary(large_data)
    del large_data  # 显式释放
    return format_report(summary)
```

---

## 3. 数据库查询优化

### 3.1 N+1 查询问题

```python
# 优化前 - N+1 查询
users = User.objects.all()
for user in users:
    print(user.profile.bio)  # 每个用户触发一次查询

# 优化后 - 预加载关联数据
users = User.objects.select_related('profile').all()
for user in users:
    print(user.profile.bio)  # 无额外查询
```

### 3.2 索引优化

```sql
-- 优化前 - 全表扫描
SELECT * FROM orders WHERE customer_email = 'test@example.com';

-- 优化后 - 添加索引
CREATE INDEX idx_orders_customer_email ON orders(customer_email);
SELECT * FROM orders WHERE customer_email = 'test@example.com';
```

### 3.3 批量操作

```python
# 优化前 - 逐条插入
for item in items:
    Item.objects.create(**item)

# 优化后 - 批量插入
Item.objects.bulk_create([Item(**item) for item in items])
```

---

## 4. 并发与异步优化

### 4.1 异步 I/O

```python
# 优化前 - 同步串行请求
import requests

def fetch_all(urls):
    results = []
    for url in urls:
        resp = requests.get(url)
        results.append(resp.json())
    return results

# 优化后 - 异步并发请求
import aiohttp
import asyncio

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [await r.json() for r in responses]
```

### 4.2 线程池处理 CPU 密集型任务

```python
# 优化前 - 串行处理
results = [heavy_compute(item) for item in data]

# 优化后 - 并行处理
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as executor:
    results = list(executor.map(heavy_compute, data))
```

---

## 5. 前端优化

### 5.1 减少 DOM 操作

```javascript
// 优化前 - 多次 DOM 操作
for (const item of items) {
  const el = document.createElement('div');
  el.textContent = item.name;
  container.appendChild(el);  // 每次触发回流
}

// 优化后 - 使用 DocumentFragment
const fragment = document.createDocumentFragment();
for (const item of items) {
  const el = document.createElement('div');
  el.textContent = item.name;
  fragment.appendChild(el);
}
container.appendChild(fragment);  // 只触发一次回流
```

### 5.2 防抖与节流

```javascript
// 防抖 - 搜索输入
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

// 节流 - 滚动事件
function throttle(fn, interval) {
  let last = 0;
  return (...args) => {
    const now = Date.now();
    if (now - last >= interval) {
      last = now;
      fn(...args);
    }
  };
}
```

### 5.3 懒加载

```javascript
// 图片懒加载
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      observer.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  observer.observe(img);
});
```

---

## 6. 缓存策略

### 6.1 函数结果缓存

```python
# 使用 lru_cache 缓存计算结果
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### 6.2 应用层缓存

```python
import redis

cache = redis.Redis()

def get_user_profile(user_id):
    cache_key = f"user:profile:{user_id}"
    cached = cache.get(cache_key)
    if cached:
        return json.loads(cached)

    profile = db.query_user_profile(user_id)
    cache.setex(cache_key, 3600, json.dumps(profile))  # 缓存1小时
    return profile
```

---

## 7. 代码优化检查清单

### 性能检查

- [ ] 是否存在不必要的嵌套循环？
- [ ] 是否使用了合适的数据结构（哈希表 vs 列表）？
- [ ] I/O 操作是否使用了批量处理？
- [ ] 是否有可以并行化的串行操作？
- [ ] 热点代码是否做了缓存？

### 内存检查

- [ ] 大数据集是否使用了流式/生成器处理？
- [ ] 是否有内存泄漏（未释放的引用、未关闭的连接）？
- [ ] 对象是否可以使用 `__slots__` 优化？

### 数据库检查

- [ ] 是否存在 N+1 查询问题？
- [ ] 高频查询字段是否建立了索引？
- [ ] 是否使用了批量操作替代循环单条操作？
- [ ] 是否有不必要的 `SELECT *`？

### 前端检查

- [ ] 是否减少了不必要的 DOM 操作？
- [ ] 高频事件是否使用了防抖/节流？
- [ ] 资源是否使用了懒加载？
- [ ] 是否开启了代码分割（Code Splitting）？

---

## 8. 性能分析工具推荐

| 语言/平台 | 工具 | 用途 |
|-----------|------|------|
| Python | `cProfile` / `line_profiler` | CPU 性能分析 |
| Python | `memory_profiler` | 内存分析 |
| Python | `py-spy` | 生产环境性能采样 |
| JavaScript | Chrome DevTools Performance | 前端性能分析 |
| JavaScript | Lighthouse | Web 性能审计 |
| Go | `pprof` | CPU/内存/协程分析 |
| Java | JProfiler / VisualVM | 全面性能分析 |
| 通用 | `flamegraph` | 火焰图可视化 |
