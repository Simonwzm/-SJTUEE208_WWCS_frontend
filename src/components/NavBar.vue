<template>
  <div class="nav w-full h-14 bg-stone fixed bg-opacity-80">
    <div class="nav-left h-full container inline-block w-1/5 text-left pl-8 text-2xl" style="font-family: 'Freehand';">NewsHub</div>
    <div class="nav-right container h-full inline-flex justify-end w-4/5 text-center items-center font-serif">
      <div class="item m-3">
        <a class="text-stonefff hover:text-stonefffff" href="#">Image Search</a>
      </div>
      <div class="item m-3 relative">
        <a class='text-stonefff hover:text-stonefffff' href="#">Text Search</a>
      </div>
      <div class="item m-3">
        <a class='text-stonefff hover:text-stonefffff' href="#">About us</a>
      </div>
      <div class="item ml-3 mr-5">
        <a class='text-stonefff hover:text-stonefffff' href="#">History</a>
      </div>
    </div>
  </div>
</template>

<script>
export default
{
  name: 'NavBar',
}
</script>

<style scoped>

.item > a {
  position: relative;
}

a::after {
  content: "";
  position: absolute;
  top: 20px;
  left: 0;
  width: 100%;
  height: 3px;
  background: #C5B358;
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 0.5s;
}

a:hover::after {
  transform-origin: left;
  transform: scaleX(1);
}

</style>
