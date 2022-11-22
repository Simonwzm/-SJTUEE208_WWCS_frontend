<template>
    <div class="shell h-full w-screen">
    <div class="left-container  w-2/3 float-left h-screen">
        <div class="search-container h-1/4 overflow-hidden">
            <InputBox style="margin-top:80px; margin-left:5px; " />
        </div>
        <div class="answer-container h-3/4 overflow-hidden  mx-4">
            <a-list item-layout="vertical" size="large" :pagination="pagination" :data-source="listData">
                <div slot="footer"><b>ant design vue</b> footer part</div>
                <a-list-item slot="renderItem" key="item.title" slot-scope="item, index">
                <!-- <template v-for="{ type, text } in actions" slot="actions">
                    <span :key="type">
                    <a-icon :type="type" style="margin-right: 8px" />
                    {{ text }}
                    </span>
                </template> -->
                <img
                    slot="extra"
                    width="272"
                    alt="logo"
                    src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
                />
                <a-list-item-meta :description="item.description">

                    <a slot="title" :href="item.href">{{ item.title }}</a>
                    <a-avatar slot="avatar" :src="item.avatar"  />
                </a-list-item-meta>
                {{ item.content }}
                </a-list-item>
            </a-list>
        </div>
    </div>
    <div class="right-container w-1/4 float-right h-full bg-black">

    </div>
    </div>
</template>
<script>
/* eslint-disable */
const listData = [];
for (let i = 0; i < 23; i++) {
  listData.push({
    href: 'https://www.antdv.com/',
    title: `ant design vue part ${i}`,
    avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    description:
      'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    content:
      'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
  });
}

export default {
    name: 'SearchView',
    components: {
        InputBox: () => import('@/components/InputBox.vue'),
    },
  data() {
    return {
      listData,
      pagination: {
        onChange: page => {
          console.log(page);
        },
        pageSize: 2,
      },
      actions: [
        { type: 'star-o', text: '156' },
        { type: 'like-o', text: '156' },
        { type: 'message', text: '2' },
      ],
    };
  },
};
</script>
<style>
/* .answer-container {
  max-width: 800px;
  margin: 0 auto;
} */
.shell {
    background-image: "@/assets/images/bg5.jpg";
    z-index:-2;
}

/* .shell:after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0px;
    right: 0px;
    background: rgba(0, 0, 0, 0.4);
    height: 100%;
    z-index: -1;
} */
</style>
