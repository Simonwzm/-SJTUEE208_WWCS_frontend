<template>
    <div class="shell h-full w-screen container" style="position:relative">
    <div class="search-container h-1/5 overflow-hidden mt-24 mx-12 z-10" style="position:sticky; top:2em;">
      <div class="main-searchbox " style="width:60%">
        <a-input-search 
        placeholder="input search loading with enterButton"  
        enter-button
        size="large"
         />
      </div>
      <div class="more-searchbox mt-6 overflow-hidden">
          <a-input-group size="large" >
          <a-row :gutter="20">
            <a-col :span="4">
              <a-input addon-before="Http://" placeholder="input website" />
            </a-col>
            <a-col :span="4">
              <a-input addon-before="title" ></a-input>
            </a-col>
            <a-col :span="4">
              <a-input addon-before="author" ></a-input>
            </a-col>
            <a-col :span="4">
              <a-date-picker placeholder="select date" />
            </a-col>
            <a-button type="primary">More</a-button>
          </a-row>

          </a-input-group>

         </div>
    </div>
    <div class="left-container h-3/4 w-2/3 float-left ml-12">
        <div class="answer-container h-3/4   ">
            <a-list item-layout="vertical" size="large" :pagination="pagination" :data-source="listData">
                <!-- <div slot="footer"><b>ant design vue</b> footer part</div> -->
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
            <!-- <a-pagination :total="50" style="margin-top: 32px; text-align: center" /> -->
            </a-list>
        </div>
    </div>
    
    <HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="80%" color=#987cb9 SIZE=1></HR>

    <div class="right-container w-1/4 float-right h-3/4 bg-black mt-6">

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
        pageSize: 4,
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
<style scoped>
/* .answer-container {
  max-width: 800px;
  margin: 0 auto;
} */
/* .shell {
    background-image: "@/assets/images/bg5.jpg";
    z-index:-2;
} */

a-input-search {

    width: 100%;
    margin: 0 auto;
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
