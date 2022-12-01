<template>
  <div id="app">
    <!-- <NavBar /> -->
    <!-- <leftSideBar /> -->
    <TestNavBar />
    <router-view/>
  </div>
</template>

<style lang="scss">

#app {
  height: 100%;
  
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
    TestNavBar: () => import('@/components/TestNavBar.vue'),
  }
}


</script>

<style>

</style>
