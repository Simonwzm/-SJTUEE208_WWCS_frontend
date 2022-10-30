<template>
  <div class="home bg-cover bg-center ">
    <div class="container">
      <div class="title">
        
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
}
</script>

<style scoped>
.home {
  height: 100vh;
  background-image: url('@/assets/bg1.png');
  position: relative;
}
.home:after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0px;
    right: 0px;
    background: rgba(0, 0, 0, 0.4);
    height: 100%;
    z-index: 1;
}

.container {
  
}
</style>