<template>
    <div class="card" v-bind:style="{ width: nowWidth + 'px' ,height: 150+'px'}" @click="sendID">
        <img :src='src' alt="Pic failed to load">
        <div class="text" >
            <h2>{{title}}</h2>
            <p style="font-size:xx-small">{{description}}</p>
        </div>
    </div>
</template>

<script>
export default 
{
    name: 'PicContainer',
    data() {
        return {

        }
    },
    props: ['nowWidth', 'title','description','url', 'id','islocal'],
    computed: {
        src() {
            if (this.islocal)  {
                return require('@/assets/' + this.url.slice(9, this.url.length));
            }
            else {
                return this.url;
            }
        }
    },
    methods: {
        sendID() {
            this.$emit('sendID', this.id);
        }
    },
}
</script>

<style scoped>
.card{
    width: auto;
    height: 200px;
    overflow: hidden;
    margin: 10px;
    background-color: #f5f4f3;
    color: #fff;
    cursor: pointer;
    position: relative;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}
.card img{
    /* width: 100%; */
    height: 100%;
    margin:auto;
    /* 设置过渡 */
    transition: 0.35s;
}
.card .text{
    position: absolute;
    top: 0px;
    left: 0px;
    bottom: 0px;
    right: 0px;
    padding: 0 18px;
    
}
.card .text::before{
    content: "";
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    left: 100%;
    /* border-left: 10px solid rgba(255,255,255); */
    background-color: rgba(255,255,255,0.5);
    opacity: 0;
    /* 过渡 */
    transition: 0.5s;
    /* 过渡延迟时间 */
    transition-delay: 0.6s;
}
.card .text h2,
.card .text p{
    margin-bottom: 6px;
    margin-left: 6px;
    opacity: 0;
    transition: 0.35s;
}
.card .text h2 {
    margin-top: 2em;
}
.card .text h2{
    font-weight: 300;
    text-transform: uppercase;
    transform: translate(30%,0%);
    transition-delay: 0.3s;
}
.card .text h2 span{
    font-weight: 800;
}
.card .text p{
    font-weight: 200;
    transform: translate(0%,30%);
}
/* 悬停样式开始 */
/* .card:hover {
   transform: scale(1.1)  
} */
.card:hover img{
    /* opacity: 0.3; */
}
.card:hover .text h2{
    opacity: 1;
    transform: translate(0%,0%);
    transition-delay: 0.4s;
}
.card:hover .text p{
    opacity: 0.5;
    transform: translate(0%,0%);
    transition-delay: 0.6s;
}
.card:hover .text::before{
    background-color: rgba(0,0,0,0.7);
    left: 0;
    opacity: 1;
    transition-delay: 0s;
}

* {
    color: #fff;
}
</style>