<template>
<div class="con">
    
    <div class="nav-left h-full inline-block w-1/5 text-left pl-8 text-2xl" style="font-family: 'Freehand';line-height: 9vh; margin-left: 20px">NewsHub</div>
    <div class="nav">
        <ul class="text-lg text-stone">
            <li><router-link to="/search">Search</router-link></li>
            <li><a href="#">Unavailable</a></li>
            <li><a href="#">Unavailable</a></li>
            <li><a href="#">Unavailable</a></li>
            <li><a href="#">Unavailable</a></li>
            <li><a href="#">Unavailable</a></li>
            <div class="nav-box"></div>
        </ul>
    </div>
  </div> 
</template>

<script>
export default {
    name: 'TestNavBar'

}
</script>

<style scoped>

        .con {
            width: 100vw;
            height: 9vh;
            background-color: rgba(255,255,255,0.8);
            /* border-radius: 10px; */
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
            height: 9vh;
            z-index: 999;
            position: absolute;
            top: 0;
            left: 0;
        } 
        .nav{
            float: right;
            width: 50vw;
            height: 100%;
            position: relative;
            margin-right: 2em;
        }
        .nav ul{
            width:100%;
            height: 100%;
            display: flex;
            align-items: center;
            /* flex-direction: row-reverse; */
            left: 5%;
        }
        .nav ul .nav-box{
            position: absolute;
            bottom: 0;
            left: 0;
            /* 如果导航栏就六个导航，那么每个导航的宽度都是整个导航
            的六分之一 */
            width: calc((100% / 6)*1);
            height: 3px;
            border-radius: 2px;
            transition: .5s;
        }
        .nav ul li{
            width: 100%;
            text-align: center;
            color: #292524;
        }
        .nav ul li a{
          
            display: block;
            width: 100%;
            height: 100%;
            line-height: 70px;
        }
        .nav ul li:nth-child(1):hover~.nav-box{
            left: calc(100% / 6 *0);
            background-color: rgb(250, 190, 250);
        }
        .nav ul li:nth-child(2):hover~.nav-box{
            left: calc(100% / 6 *1);
            background-color: rgb(126, 193, 245);
        }
        .nav ul li:nth-child(3):hover~.nav-box{
            left: calc(100% / 6 *2);
            background-color: #d18df8;
        }
        .nav ul li:nth-child(4):hover~.nav-box{
            left: calc(100% / 6 *3);
            background-color: #ffb1b1;
        }
        .nav ul li:nth-child(5):hover~.nav-box{
            left: calc(100% / 6 *4);
            background-color: #8da1f8;
        }
        .nav ul li:nth-child(6):hover~.nav-box{
            left: calc(100% / 6 *5);
            background-color: #7df88e;
        }
</style>