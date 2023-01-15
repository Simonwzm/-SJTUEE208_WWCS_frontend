<template>
  <div class="clearfix" style="width: 200px;height:200px;">
    <a-upload
      action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
      list-type="picture-card"
      :customRequest = 'imgAdd'
      :file-list="fileList"
      @preview="handlePreview"
      @change="handleChange"
      class="pic-uploader"
      style="width: 100%; height:100%"
    >
      <div v-if="(fileList.length < 1)" style="width:200px; height:200px;">
        <a-icon type="plus"  style="margin-top:45px;margin-bottom:-20px; width: 80px;height:80px" />
        <div class="ant-upload-text" style="width:60px;height:60px;font-size:16px;margin-bottom:20px;margin-left:auto;margin-right:auto;">
          Upload
        </div>
      </div>
    </a-upload>
    <a-modal :visible="previewVisible" :footer="null" @cancel="handleCancel" style='width:100%;height:100%;'>
      <img alt="example" style="width: 100%" :src="previewImage" />
    </a-modal>
  </div>
</template>
<script>
function getBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
  });
}
export default {
  data() {
    return {
      previewVisible: false,
      previewImage: '',
      fileList: [
        {
          uid: '-1',
          name: 'image.png',
          status: 'done',
          url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
        },
        // {
        //   uid: '-2',
        //   name: 'image.png',
        //   status: 'done',
        //   url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
        // },
        // {
        //   uid: '-3',
        //   name: 'image.png',
        //   status: 'done',
        //   url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
        // },
        // {
        //   uid: '-4',
        //   name: 'image.png',
        //   status: 'done',
        //   url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
        // },
        // {
        //   uid: '-5',
        //   name: 'image.png',
        //   status: 'error',
        // },
      ],
    };
  },
  methods: {
    handleCancel() {
      this.previewVisible = false;
    },
    imgAdd(data) {

      const formData = new FormData();
      formData.append('file', data.file);
      console.log(formData.get('file')); //FormData私有类对象，访问不到，可以通过get判断值是否传进去
      let that = this
      this.$axios.post('http://127.0.0.1:5000/upload',formData,{headers:{'Content-Type':'application/x-www-form-urlencoded' }}, ) //请求头要为表单
        .then(response=>{
          // console.log(response.data);
          data.onSuccess(response.data)
			console.log('success')
        that.$emit('func', response)
          })
          .catch(function (error) {
            console.log(error);
			console.log('error')
          })
        },
    async handlePreview(file) {
      if (!file.url && !file.preview) {
        file.preview = await getBase64(file.originFileObj);
      }
      this.previewImage = file.url || file.preview;
      this.previewVisible = true;
    },
    handleChange({ fileList }) {
      this.fileList = fileList;
    },
  },
};
</script>
<style>

.clearfix {
    width: 200px;
    height: 200px;
}

/* a-upload{
    width: 100px;
    height: 100px;
} */
/* you can make up upload button and sample style by using stylesheets */
.ant-upload-select-picture-card i {
  font-size: 45px;

    width: 200px;
    height: 200px;
  /* color: #999; */

}
.pic-uploader > .ant-upload {
    width: 200px;
    height: 200px;
  background:
      linear-gradient(217deg, rgba(255,0,0,.5), rgba(255,0,0,0) 70.71%),
      linear-gradient(127deg, rgba(0,255,0,.5), rgba(0,255,0,0) 70.71%),
      linear-gradient(336deg, rgba(0,0,255,.5), rgba(0,0,255,0) 70.71%);
    border-radius: 8px;
}

.ant-upload-select-picture-card .ant-upload-text {
  margin-top: 8px;
  color: #666;
}
</style>
