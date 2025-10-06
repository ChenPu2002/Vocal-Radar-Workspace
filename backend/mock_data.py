from models import User, Post, Comment
from datetime import datetime, timedelta
import random

# 模拟用户数据
users = [
    User(
        id=1,
        nickname="小米发烧友",
        avatar="https://i.pravatar.cc/150?img=1",
        bio="资深小米用户，喜欢折腾各种ROM"
    ),
    User(
        id=2,
        nickname="华为老用户",
        avatar="https://i.pravatar.cc/150?img=2",
        bio="用了5年华为，见证了华为的成长"
    ),
    User(
        id=3,
        nickname="OPPO拍照达人",
        avatar="https://i.pravatar.cc/150?img=3",
        bio="热爱手机摄影，OPPO Find系列忠实用户"
    ),
    User(
        id=4,
        nickname="vivo音乐控",
        avatar="https://i.pravatar.cc/150?img=4",
        bio="HiFi音质爱好者，vivo X系列粉丝"
    ),
    User(
        id=5,
        nickname="一加极客",
        avatar="https://i.pravatar.cc/150?img=5",
        bio="追求性能与流畅，一加氢OS深度用户"
    )
]

# 帖子主题和内容模板
post_templates = [
    {
        "title": "小米13 Pro信号问题终于解决了！",
        "content": "之前一直被信号问题困扰，升级到最新版MIUI 14.0.5后，信号明显改善。电梯里也能正常接电话了，分享给大家！",
        "media_type": "image",
        "tags": ["信号", "系统更新"]
    },
    {
        "title": "华为Mate 50续航太强了",
        "content": "从早上8点到晚上10点，中度使用还剩35%电量。这续航表现在旗舰机里算是顶级的了。而且充电速度也很快，66W快充半小时就能充到80%。",
        "media_type": "image",
        "tags": ["续航", "充电"]
    },
    {
        "title": "OPPO Find X6 Pro夜拍样张分享",
        "content": "昨晚拍的夜景，一亿像素主摄+哈苏调色真的绝了！细节保留很好，噪点控制也不错。放几张原图给大家看看。",
        "media_type": "image",
        "tags": ["拍照", "夜拍"]
    },
    {
        "title": "vivo X90 Pro+音质体验",
        "content": "作为一个音乐发烧友，X90 Pro+的CS43131双DAC芯片真的没让我失望。搭配我的森海塞尔IE800，听感细腻，解析力强。",
        "media_type": "video",
        "tags": ["音质", "HiFi"]
    },
    {
        "title": "一加11性能测试：原神实测",
        "content": "骁龙8 Gen2+满血版LPDDR5X+UFS4.0，跑原神须弥城最高画质，帧率稳定在59-60fps，温度控制在42度左右。这散热真的可以！",
        "media_type": "video",
        "tags": ["性能", "游戏"]
    },
    {
        "title": "ColorOS 13.1更新体验",
        "content": "刚更新完ColorOS 13.1，流畅度提升明显，动画更跟手了。还有新增的隐私安全功能，可以看到哪些应用在后台调用权限。",
        "media_type": "image",
        "tags": ["系统更新", "流畅度"]
    },
    {
        "title": "小米路由器AX9000配对小米手机",
        "content": "家里换了AX9000后，小米手机连WiFi速度明显快了。5G频段实测下载速度能到600Mbps+，打游戏延迟也降低了。",
        "media_type": "image",
        "tags": ["WiFi", "网络"]
    },
    {
        "title": "华为P60系列摄影技巧分享",
        "content": "用P60 Pro拍了一个月，总结了一些摄影技巧。主要是XMAGE影像的使用心得，包括光圈模式、夜景模式等。有需要的朋友可以参考。",
        "media_type": "image",
        "tags": ["拍照", "技巧"]
    },
    {
        "title": "OPPO超级闪充实测",
        "content": "100W SuperVOOC超级闪充真的快！从0%充到100%只要25分钟。而且充电时手机不烫，这个电荷泵技术确实厉害。",
        "media_type": "video",
        "tags": ["充电", "快充"]
    },
    {
        "title": "vivo折叠屏X Fold2使用一个月感受",
        "content": "折痕控制得很好，展开后基本看不出来。悬停功能很实用，拍照、看视频都方便。就是有点重，单手操作比较累。",
        "media_type": "image",
        "tags": ["折叠屏", "使用体验"]
    },
    {
        "title": "一加Ace 2性价比之选",
        "content": "2000价位段性价比真的高。骁龙8+、5000mAh大电池、长寿版100W快充，日常使用完全够用。推荐给预算有限的朋友。",
        "media_type": "image",
        "tags": ["性价比", "推荐"]
    },
    {
        "title": "小米澎湃OS初体验",
        "content": "从MIUI升级到澎湃OS，最大的感受是更流畅了，UI设计也更现代化。还有人车家全生态互联，体验提升很大。",
        "media_type": "image",
        "tags": ["系统", "生态"]
    },
    {
        "title": "华为鸿蒙4.0新功能解析",
        "content": "鸿蒙4.0带来了很多实用新功能，比如超级中转站、智慧多窗等。分布式能力也更强了，手机和平板协同办公很方便。",
        "media_type": "video",
        "tags": ["鸿蒙", "系统更新"]
    },
    {
        "title": "OPPO Find N3折叠屏开箱",
        "content": "刚入手Find N3，外观真的惊艳！展开是8英寸大屏，折叠后是正常手机大小。铰链阻尼感很好，可以任意角度悬停。",
        "media_type": "image",
        "tags": ["开箱", "折叠屏"]
    },
    {
        "title": "vivo X100 Pro影像系统深度体验",
        "content": "天玑9300+蔡司光学镜头，拍照体验真的是旗舰级。人像模式下的虚化效果自然，逆光HDR也处理得很好。",
        "media_type": "image",
        "tags": ["拍照", "影像"]
    },
    {
        "title": "一加12屏幕素质真不错",
        "content": "2K+120Hz LTPO屏幕，峰值亮度4500nit。室外阳光下也能看清屏幕，色彩还原准确。护眼模式下长时间看书眼睛也不累。",
        "media_type": "image",
        "tags": ["屏幕", "显示"]
    },
    {
        "title": "小米13 Ultra徕卡影像体验",
        "content": "徕卡联名的影像系统确实有独到之处。徕卡经典和徕卡生动两种风格，拍出来的照片质感很好。可变光圈也很实用。",
        "media_type": "image",
        "tags": ["拍照", "徕卡"]
    },
    {
        "title": "华为Mate 60 Pro卫星通信实测",
        "content": "在没有信号的山区测试了卫星通信功能，真的能用！虽然速度慢，但关键时刻能救命。这个黑科技必须点赞。",
        "media_type": "video",
        "tags": ["卫星通信", "黑科技"]
    },
    {
        "title": "OPPO Reno11系列人像算法升级",
        "content": "新的人像算法很自然，不会过度磨皮。肤色还原准确，发丝细节保留得也好。自拍党的福音！",
        "media_type": "image",
        "tags": ["自拍", "人像"]
    },
    {
        "title": "vivo S18系列前置柔光灯体验",
        "content": "前置双柔光灯在暗光环境下自拍效果很好，光线柔和不刺眼。补光均匀，拍出来的照片很自然。",
        "media_type": "image",
        "tags": ["自拍", "补光"]
    }
]

# 生成帖子
posts = []
post_id = 1
for user in users:
    # 每个用户生成12-18条帖子
    num_posts = random.randint(12, 18)
    for i in range(num_posts):
        template = random.choice(post_templates)
        
        # 生成媒体URL
        media_urls = []
        if template["media_type"] == "image":
            num_images = random.randint(1, 4)
            media_urls = [f"https://picsum.photos/800/600?random={post_id * 10 + j}" for j in range(num_images)]
        elif template["media_type"] == "video":
            media_urls = [f"https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"]
        
        # 生成时间（最近30天内的随机时间）
        days_ago = random.randint(0, 30)
        hours_ago = random.randint(0, 23)
        created_at = datetime.now() - timedelta(days=days_ago, hours=hours_ago)
        
        post = Post(
            id=post_id,
            user_id=user.id,
            title=template["title"],
            content=template["content"],
            media_type=template["media_type"],
            media_urls=media_urls,
            likes=random.randint(10, 1000),
            comments_count=random.randint(0, 50),
            created_at=created_at
        )
        posts.append(post)
        post_id += 1

# 评论内容模板
comment_templates = [
    "同感！我也遇到过类似的问题",
    "太有用了，谢谢分享！",
    "请问楼主用的什么版本？",
    "这个确实不错，已经按照你说的操作了",
    "我这边情况不一样，还是有问题",
    "期待后续更新能解决",
    "非常详细的评测，赞一个！",
    "这个功能我也在用，确实很方便",
    "有没有视频教程？",
    "我的型号不支持，羡慕了",
    "这个技巧太实用了！",
    "已收藏，慢慢研究",
    "楼主能多分享点吗？",
    "我也想换这款手机了",
    "性价比确实挺高的"
]

# 生成评论
comments = []
comment_id = 1
for post in posts:
    # 每个帖子生成0-8条评论
    num_comments = random.randint(0, min(8, post.comments_count))
    for i in range(num_comments):
        # 随机选择一个用户作为评论者（不能是帖子作者）
        comment_user = random.choice([u for u in users if u.id != post.user_id])
        
        # 生成评论时间（晚于帖子创建时间）
        max_hours = int((datetime.now() - post.created_at).total_seconds() / 3600)
        if max_hours > 0:
            hours_after = random.randint(1, min(max_hours, 72))
            comment_created_at = post.created_at + timedelta(hours=hours_after)
        else:
            comment_created_at = post.created_at + timedelta(minutes=random.randint(10, 120))
        
        comment = Comment(
            id=comment_id,
            post_id=post.id,
            user_id=comment_user.id,
            content=random.choice(comment_templates),
            created_at=comment_created_at
        )
        comments.append(comment)
        comment_id += 1

