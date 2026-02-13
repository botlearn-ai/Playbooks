/**
 * 代码优化示例 - JavaScript 版本
 * 演示前端和 Node.js 常见的优化模式
 */

// =============================================================================
// 示例 1: 数组操作优化
// =============================================================================

// 优化前 - 多次遍历
function getActiveUserEmails_slow(users) {
  return users
    .filter((u) => u.active)
    .map((u) => u.email)
    .filter((email) => email.endsWith("@company.com"));
}

// 优化后 - 单次遍历使用 reduce
function getActiveUserEmails_fast(users) {
  const results = [];
  for (const u of users) {
    if (u.active && u.email.endsWith("@company.com")) {
      results.push(u.email);
    }
  }
  return results;
}

// =============================================================================
// 示例 2: 对象查找优化
// =============================================================================

// 优化前 - 每次用 find 查找 O(n)
function getUserById_slow(users, id) {
  return users.find((u) => u.id === id);
}

// 优化后 - 预建索引 O(1)
function buildUserIndex(users) {
  const index = new Map();
  for (const user of users) {
    index.set(user.id, user);
  }
  return index;
}

// =============================================================================
// 示例 3: 防抖优化
// =============================================================================

function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

// 用法: 搜索框输入时避免频繁请求
// const search = debounce((query) => fetchResults(query), 300);

// =============================================================================
// 示例 4: 对象池模式 - 避免频繁 GC
// =============================================================================

class ObjectPool {
  constructor(factory, reset, initialSize = 10) {
    this.factory = factory;
    this.reset = reset;
    this.pool = [];
    for (let i = 0; i < initialSize; i++) {
      this.pool.push(factory());
    }
  }

  acquire() {
    return this.pool.length > 0 ? this.pool.pop() : this.factory();
  }

  release(obj) {
    this.reset(obj);
    this.pool.push(obj);
  }
}

// 用法: 高频创建的临时对象
// const vecPool = new ObjectPool(
//   () => ({ x: 0, y: 0 }),
//   (v) => { v.x = 0; v.y = 0; }
// );

// =============================================================================
// 示例 5: 虚拟列表 - 大量 DOM 元素优化
// =============================================================================

class VirtualList {
  constructor(container, items, itemHeight, renderItem) {
    this.container = container;
    this.items = items;
    this.itemHeight = itemHeight;
    this.renderItem = renderItem;

    this.totalHeight = items.length * itemHeight;
    this.visibleCount = Math.ceil(container.clientHeight / itemHeight) + 2;

    this.setup();
  }

  setup() {
    this.container.style.overflow = "auto";
    this.container.style.position = "relative";

    this.spacer = document.createElement("div");
    this.spacer.style.height = `${this.totalHeight}px`;
    this.container.appendChild(this.spacer);

    this.container.addEventListener("scroll", () => this.onScroll());
    this.onScroll();
  }

  onScroll() {
    const scrollTop = this.container.scrollTop;
    const startIdx = Math.floor(scrollTop / this.itemHeight);
    const endIdx = Math.min(startIdx + this.visibleCount, this.items.length);

    // 只渲染可见范围内的元素
    const fragment = document.createDocumentFragment();
    for (let i = startIdx; i < endIdx; i++) {
      const el = this.renderItem(this.items[i], i);
      el.style.position = "absolute";
      el.style.top = `${i * this.itemHeight}px`;
      fragment.appendChild(el);
    }

    // 清除旧元素，添加新元素
    while (this.spacer.firstChild) {
      this.spacer.removeChild(this.spacer.firstChild);
    }
    this.spacer.appendChild(fragment);
  }
}

// =============================================================================
// 示例 6: Promise 并发控制
// =============================================================================

async function parallelLimit(tasks, concurrency) {
  const results = [];
  const executing = new Set();

  for (const [index, task] of tasks.entries()) {
    const promise = task().then((result) => {
      executing.delete(promise);
      results[index] = result;
    });
    executing.add(promise);

    if (executing.size >= concurrency) {
      await Promise.race(executing);
    }
  }

  await Promise.all(executing);
  return results;
}

// 用法: 限制并发请求数
// const tasks = urls.map(url => () => fetch(url).then(r => r.json()));
// const results = await parallelLimit(tasks, 5);  // 最多5个并发

module.exports = {
  getActiveUserEmails_slow,
  getActiveUserEmails_fast,
  buildUserIndex,
  debounce,
  ObjectPool,
  parallelLimit,
};
