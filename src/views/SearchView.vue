<template>
    <div class="shell h-full w-screen container" style="position:relative">
    <div class="search-container h-1/5 overflow-hidden mt-24 mx-12 z-10" style="position:sticky; top:calc(2em - 8px);">
      <div class="main-searchbox " style="width:100%">
        <div class="c" style="width:60%;">

        <a-input-search 
        placeholder="input search loading with enterButton"  
        enter-button
		@search="onSearch"
        size="large"
		v-model="searchInput"
         />


        </div>
         <div class="btnBox" style="width:35%; float:right; display:flex;justify-content: space-evenly;">

           <a-button class="test-button" @click="changeList" >test switch</a-button>
           <a-button class="test-button" @click="changeList" >test switch</a-button>
           <a-button class="test-button" @click="changeList" >test switch</a-button>
         </div>
        </div>
      <div class="more-searchbox mt-6 h-3/4 ">
          <a-input-group size="large" >
          <a-row :gutter="20">
            <a-col :span="4">
              <a-input addon-before="Http://" placeholder="input website" v-model="url"/>
            </a-col>
            <a-col :span="4">
              <a-input addon-before="title" v-model="title"></a-input>
            </a-col>
            <a-col :span="4">
              <a-date-picker valueFormat="YYYY-MM-DD" placeholder="select date" v-model="date"/>
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
        <div class="pic-container overflow-y-scroll container" style="height:580px;	display: flex;flex-wrap: wrap;padding: 5px;" v-if="!isListAnswer">
            <PicContainer
                v-for="(item,index) in picUrlArr" 
                :key="index"
                :nowWidth="item.nowWidth"
                :title="item.title"
                :description="item.description"
                :url="item.url"
                style="display:flex;flex-grow: 1;margin: 10px;"
                >
            </PicContainer>
            <!-- <div class="rowContainer" v-for="(thing, index) in picRow" :key="index">
              <PicContainer
                v-for="(item,index) in thing['picList']"
                :key="index"
                :props="item"
                >
            </PicContainer>
            
            </div> -->

        </div>
    </div>
    
    <!-- <HR style="z-index: -1;FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="80%" color=#987cb9 SIZE=1></HR> -->
    <HR style="z-index: -1;"></HR>

    <div class="right-container w-1/4 mx-12 float-right h-3/4 " style="width:30%;">
      <div style="margin-top:-44px; z-index:12;">
          <a-tabs default-active-key="1" @change="callback" style="z-index:12">
            <a-tab-pane key="1" tab="extension 1" style="z-index:12">
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
            <a-tab-pane key="2" tab="extension 2" force-render style="z-index:12">
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
            <a-tab-pane key="3" tab="extension 3" style="z-index:12">
              Content of Tab Pane 3
            </a-tab-pane>
          </a-tabs>
        </div>
    </div>
    </div>
</template>
<script>
/* eslint-disable */
// const listData = [];

import axios from 'axios';
export default {
    name: 'SearchView',
    components: {
        // InputBox: () => import('@/components/InputBox.vue'),
        PicContainer: () => import('@/components/PicContainer.vue'),
    },
  data() {
    return {
		searchInput: '',
		url:'',
		title:'',
		date:undefined,
      picUrlArr: [
        {url:'@/assets/bg01.jpg', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg02.jpg', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg03.jpg', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/logo.png', title:'1', description:'2', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg1.png', title:'1', description:'2', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg2.png', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg3.png', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg01.jpg', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg02.jpg', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg03.jpg', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/logo.png', title:'1', description:'2', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg1.png', title:'1', description:'2', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg2.png', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
        {url:'@/assets/bg3.png', title:'1', description:'1', originalWidth:NaN, nowWidth:NaN},
    ],
      // picRow: [{picList:[{url:'@/assets/bg01.jpg', title:'', description:''}], height:'',},{picList:[{url:'@/assets/bg01.jpg', title:'', description:''}], height:'',}], // 
      referHight: 150,  // refer height for each pic in const height waterfall layout

      listData: [],
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
  computed: {
    hasTitle() {
      if (this.title == '') {
        return false;
      } else {
        return true;
      }
    },
    hasChinese() {
      var pattern = new RegExp("[\u4E00-\u9FA5]+");
      if (pattern.test(this.searchInput) || pattern.test(this.title)) {
        return true;
      } else {
        return false;
      }
    },
  },
  methods: {

	// get the value in inputbox
	onSearch(){
		//alert(this.searchInput);
		//alert(this.url);
		//alert(this.title);
		//alert(this.date);
    let that = this;

    var pattern = new RegExp("[\u4E00-\u9FA5]+");
    console.log(this.hasTitle)
		axios.post('http://127.0.0.1:5000/search', {
			url: this.url,
			title: this.title,
			date: this.date,
      hasTitle: this.hasTitle,
			keyword: this.searchInput,
      
		})
		.then(function (response) {
      console.log(response)
      for (let el in response.data) {
        console.log(response.data[el])
        let ava = ''
        if (response.data[el].source == 'cnn') {
          let ava = '@/assets/avatar/CNN.jpg'
        }
        else if (response.data[el].source == 'sina') {
          let ava = '@/assets/avatar/sina.jpg'
        }
        else if (response.data[el].source == 'stdaily') {
          let ava = '@/assets/avatar/stdaily.jpg'
        }
        that.listData.push({
          href: response.data[el].url,
          title: response.data[el].title,
          avatar:ava,
          content: that.hasChinese? response.data[el].content : response.data[el].contentEnglish,
        });
      }
		})
	},
	test(){
    let that = this
    this.$http.post('http://127.0.0.1:5000/search')
		.then(response => {
      for (let i = 0; i < 23; i++) {
        console.log('here')
        that.listData.push({
          href: 'https://www.antdv.com/',
          title: `ant design vue part ${i}`,
          avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
          description:
            'Ant Design, a design language for background applications, is refined by Ant UED Team.',
          content:
            'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
        });
}
		})
	},

    callback(key) {
      console.log(key);
    },

    getPicUrl() {
      axios.get('http://localhost:8080/picUrl').then((res) => {
        console.log(res.data);
        this.picUrlArr = res.data;
      });
    },

    // read all url in picUrlArr and record their originalWidth
    getPicWidth() {
      for (let i = 0; i < this.picUrlArr.length; i++) {
        const img = new Image();
        img.src = require('@/assets/'+this.picUrlArr[i].url.slice(9, this.picUrlArr[i].url.length));
        img.onload = () => {
          this.picUrlArr[i].originalWidth = img.width;
          // this.picUrlArr[i].nowWidth = img.width;
          console.log(i, img.width)
        };
      }
      console.log('read width done')
    },

    //scale the image to reference height
    scalePic() {
      for (let i = 0; i < this.picUrlArr.length; i++) {
        this.picUrlArr[i].nowWidth = this.picUrlArr[i].originalWidth * this.referHight / this.picUrlArr[i].originalHeight;
      }
      console.log('scaled:')
      console.log(this.picUrlArr  )
    },

    changeList() {
      // getPicUrl();
      this.getPicWidth();
      this.scalePic();
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

.pic-container::after {
		content: '';
		flex-grow: 99999;
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
