<template>
    <div class="shell h-full w-screen container" style="position:relative">
    <div class="search-container h-1/5 overflow-hidden mt-24 mx-12 z-10" style="position:sticky; top:2em;">
      <div class="main-searchbox " style="width:60%">
        <a-input-search 
        placeholder="input search loading with enterButton"  
        enter-button
        size="large"
         />
      <a-button class="test-button" @click="changeList" style="width:30%; float:right;">test switch</a-button>
      </div>
      <div class="more-searchbox mt-6 h-3/4 ">
          <a-input-group size="large" >
          <a-row :gutter="20">
            <a-col :span="4">
              <a-input addon-before="Http://" placeholder="input website" />
            </a-col>
            <a-col :span="4">
              <a-input addon-before="title" ></a-input>
            </a-col>
            <a-col :span="4">
              <a-date-picker placeholder="select date" />
            </a-col>
            <a-button type="primary">More</a-button>
          </a-row>

          </a-input-group>

         </div>
    </div>
    <div class="left-container h-3/4 float-left ml-12" style='width:60%;'>
        <div class="answer-container overflow-y-scroll" style="height:580px;" v-if="isListAnswer">
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
        <div class="pic-container overflow-y-scroll bg-black" style="height:580px;" v-if="!isListAnswer">
        </div>
    </div>
    
    <HR style="z-index: -1;FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="80%" color=#987cb9 SIZE=1></HR>

    <div class="right-container w-1/4 mx-12 float-right h-3/4 " style="width:30%;">
      <div style="margin-top:-44px; z-index:12;">
          <a-tabs default-active-key="1" @change="callback" style="z-index:12">
            <a-tab-pane key="1" tab="Tab 1" style="z-index:12">
              <a-card hoverable style="width: 300px">
                  <img
                    slot="cover"
                    alt="example"
                    src="https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png"
                  />
                  <template slot="actions" class="ant-card-actions">
                    <a-icon key="setting" type="setting" />
                    <a-icon key="edit" type="edit" />
                    <a-icon key="ellipsis" type="ellipsis" />
                  </template>
                  <a-card-meta title="Card title" description="This is the description">
                    <a-avatar
                      slot="avatar"
                      src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                    />
                  </a-card-meta>
                </a-card>
            </a-tab-pane>
            <a-tab-pane key="2" tab="Tab 2" force-render style="z-index:12">
              <template>
                <a-card hoverable style="width: 240px">
                  <img
                    slot="cover"
                    alt="example"
                    src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
                  />
                  <a-card-meta title="Europe Street beat">
                    <template slot="description">
                      www.instagram.com
                    </template>
                  </a-card-meta>
                </a-card>
              </template>

            </a-tab-pane>
            <a-tab-pane key="3" tab="Tab 3" style="z-index:12">
              Content of Tab Pane 3
            </a-tab-pane>
          </a-tabs>
        </div>
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
      isListAnswer: true,
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
  methods: {
    callback(key) {
      console.log(key);
    },
    changeList() {
      this.isListAnswer = !this.isListAnswer;
    },
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
*::-webkit-scrollbar {
    display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
*{
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
}

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
