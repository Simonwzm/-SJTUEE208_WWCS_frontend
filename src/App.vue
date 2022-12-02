<template>
  <div id="app">
    <!-- <NavBar /> -->
    <!-- <leftSideBar /> -->
    <TestNavBar />
    <router-view/>
    <!-- <PicContainer /> -->
  </div>
</template>

<style lang="scss">

#app {
  height: 100%;
  
}

*::-webkit-scrollbar {
    display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
*{
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
}
router-view {
  overflow-x:hidden;
}
</style>

<script>
export default 
{
  name: 'App',
  components: 
  {
    NavBar: () => import('@/components/NavBar.vue'),
    leftSideBar: () => import('@/components/LeftSideBar.vue'),
    // PicContainer: () => import('@/components/PicContainer.vue'),
    TestNavBar: () => import('@/components/TestNavBar.vue'),
  }
}


</script>

<style>

</style>
