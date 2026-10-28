# data.huiying

**huiying canonical product database** — MkDocs 子站，产品数据唯一事实源（machine-readable）。

定位：被检索、被机器读、被引用的基础数据支撑。纯结构化数据 / 规格 / 交叉引用，**内容零营销**，与主站 `carfilterspro.com` 营销文案零重复。

## 目录结构

```
data.huiying/
├── mkdocs.yml                  # MkDocs Material 配置 + nav（品牌 navy/orange 同色系）
├── requirements.txt            # mkdocs / mkdocs-material
├── data/
│   ├── products.json           # ★ 权威数据集（canonical，与主站 src/data/products.json 字节一致）
│   ├── fitment.json            # ★ 车型适配参考框架（reference-only，非 OE 精确对照）
│   ├── sku-oe-vehicle.json     # ★ SKU–OE–车型关联（source-verified OE↔brand + reference 车型）
│   ├── oe-patterns.json        # OE 号前缀模式框架（prefix-pattern reference）
│   ├── size-ranges.json        # 尺寸参考区间库（按车辆级别 / 机滤螺纹）
│   ├── replacement-intervals.json # 替换周期参考数据（五类滤芯）
│   └── procurement.json        # HS 编码 + MOQ/包装参考框架
├── scripts/
│   ├── build-fitment-pages.py  # ★ 从 JSON 生成全部数据页（零手工抄写）
│   └── build-sku-oe-vehicle.py # ★ 生成 SKU–OE–车型关联数据集 + 页面
├── overrides/
│   └── main.html               # announce 回链主站 + Organization JSON-LD
└── docs/
    ├── index.md                # 首页：定位 / 覆盖范围 / 诚实口径
    ├── products/
    │   ├── index.md            # SKU 全量索引（生成）
    │   ├── {slug}.md           # 5 品类页（生成）
    │   └── {model}.md          # 10 SKU 参数页（生成）
    ├── fitment/                # 车型适配参考框架（生成）
    │   ├── index.md
    │   └── {type}.md           # air / oil / cabin / fuel / wiper 各一
    ├── materials/
    │   └── media-comparison.md # 滤材对比（手写：纤维素/混纺/合成/纳米 + 活性炭/玻纤/驻极）
    ├── reference/              # 参考数据页（生成）
    │   ├── oe-patterns.md      # OE 前缀模式框架
    │   ├── size-ranges.md      # 尺寸区间库
    │   ├── replacement-intervals.md # 替换周期
    │   └── procurement.md      # 采购参考
    ├── specification/          # 数据规范（手写）
    │   ├── field-schema.md
    │   ├── data-status.md
    │   ├── sources.md
    │   └── changelog.md
    ├── llms.txt                # llmstxt.org 规范
    └── robots.txt
```

## 数据一致性机制（核心约束）

1. **唯一事实源**：主站 `src/data/products.json` 是 SKU 身份字段的唯一真值表。
2. **权威副本同值**：本仓 `data/products.json` 与主站 `src/data/products.json` **字节一致**。
3. **零手工抄写**：数据页全部由 `scripts/build-fitment-pages.py` 渲染生成，不手工转录任何数值。
4. **零编造**：源数据缺失的规格字段（尺寸/材质/效率/OE/装箱/HS）一律标 `NEEDS_VERIFICATION`，适配框架标 `reference`，绝不杜撰精确 OE 号或尺寸。

## 同步流程（主站改数据 → 本仓重建）

```bash
# 1. 主站 Huiying 改 src/data/products.json 后复制入本仓（保证同值）
cp ../Huiying/src/data/products.json data/products.json

# 2. 校验两仓字节一致
diff data/products.json ../Huiying/src/data/products.json && echo IDENTICAL

# 3. 重建全部数据页
python3 scripts/build-fitment-pages.py

# 4. 本地构建验证
mkdocs build

# 5. 提交推送
git add -A && git commit -m "data: rebuild from products.json vX.Y.Z" && git push
```

> 新增/删除 SKU 时，除跑脚本外，还需同步 `mkdocs.yml` 的 `nav.SKU Details` 分组。

## 本地运行

```bash
pip install -r requirements.txt
python3 scripts/build-fitment-pages.py
mkdocs serve          # http://127.0.0.1:8000
mkdocs build          # 静态输出 site/
```
