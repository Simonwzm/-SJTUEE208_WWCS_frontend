<template>
<div class="shell">
  <div class="home bg-cover bg-center ">
      <!-- <div class="seperate-line"></div> -->
      <div class="container mx-auto mt-56 font-serif">
        <div class = "title text-7xl text-center text-stone tracking-wide font-thin">Welcome to NewsHub</div> 
        <br />
        <div class="subtitle text-2xl text-center text-stonef font-thin">
            The next generation of web-based news aggregator 
        </div>
        <div class="subtitle text-2xl text-center text-stonef">
          See more information about us below
        </div>
      </div>
      <InputBox id="1" style="margin-top:60px" />
  </div>
</div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    InputBox: () => import('@/components/InputBox.vue'),
  }
}
</script>

<style scoped>
.home {
  height: 100vh;
  width:100%;
  background-image: url('@/assets/bg1.png');
  position: absolute;
  top:0;
  left:0;
  z-index: -2;
}
.home:after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0px;
    right: 0px;
    background: rgba(0, 0, 0, 0.4);
    height: 100%;
    z-index: -1;
}

/* .shell {
  width:100%;
  height:100vh;
  position: relative;
} */

</style>