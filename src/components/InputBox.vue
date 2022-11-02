<template>
    <div class="input-container container w-1/2 relative mx-auto">
        <input id='2' type="text" placeholder="ttt" class="input-fill form-input border-bottom text-gold font-serif text-2xl" @change="changeFlag">
        <label class="text-gold input-lable w-full text-center font-serif text-2xl font-thin"  id="1" >Click here to begin search</label>
        <span class="border-bottom-animation center"></span>
    </div>
</template>

<script>
export default {
    name: 'InputBox',
    data() {
        return {
            flag:false,
        }
    },
    methods: {
        changeFlag() {
            let inputbox = document.getElementById('2')
            if (inputbox.value == '') {
                this.flag=true
                inputbox.classList.remove('filled')
            }
            else {
                this.flag=false
                inputbox.classList.add('filled')
            }
        }
    }


    // data() {
    //     return {
    //         placeHolder: 'testtesttest',

    //     }
    // },
    // methods: {
    //     changePlaceholder(event) {
            
    //         let focusedElement = document.activeElement

    //         console.log('1')
    //         let inputbox = document.getElementById('1');
    //         console.log(inputbox.placeholder)
    //         if (inputbox===focusedElement) {
    //             this.placeHolder = 'testtesttest '
    //         }
    //         else {
    //             this.placeHolder = 'testtesttest'
    //             console.log(inputbox.placeHolder)
    //                 focusedElement.setAttribute('placeholder', '')
    //         }
    //         return event
    //     }
    // }
}
</script>

<style scoped>

.form-input {
  position: relative;
  /* font-family: "Source Sans Pro", sans-serif; */
  /* font-weight: 600; */
  width: 100%;
  height: 40px;
  
  border: none;
  padding: 0 10px;
  box-shadow: none;
  outline: none;
  -webkit-transition: all .5s ease;
     -moz-transition: all .5s ease;
      -ms-transition: all .5s ease;
       -o-transition: all .5s ease;
          transition: all .5s ease;
}
.form-input.border-bottom {
  position: relative;
  background: transparent;
  padding: 0;
  border-bottom: 2px solid rgb(214, 211, 209, 0.2);
}
.form-input.border-bottom ~ .border-bottom-animation {
  position: absolute;
  content: "";
  width: 0;
  background: rgba(0, 0, 0, .1);
  height: 2px;
  z-index: 99;
  -webkit-transition: all .5s ease;
     -moz-transition: all .5s ease;
      -ms-transition: all .5s ease;
       -o-transition: all .5s ease;
          transition: all .5s ease;
}
/* Border bottom center */
.form-input.border-bottom ~ .border-bottom-animation.center {
  left: 0;
  right: 0;
  bottom: 0;
  margin: 0 auto;
}
.form-input.border-bottom:focus ~ .border-bottom-animation.center {
  background: #C5B358;
  width: 120%;
  left: -10%;
}
.form-input.border-bottom.filled ~ .border-bottom-animation.center {
  background: rgb(214, 211, 209, .5);
  width: 120%;
  left: -10%;
  -webkit-transition: all .5s ease;
     -moz-transition: all .5s ease;
      -ms-transition: all .5s ease;
       -o-transition: all .5s ease;
          transition: all .5s ease;
}

.form-input.border-bottom.filled {
    border: none;
}
.form-input.border-bottom.filled:focus ~ .border-bottom-animation.center {
  background: #C5B358;
  width: 120%;
  left: -10%;
}
::-webkit-input-placeholder {
text-align: center;
}
:-moz-placeholder {
text-align: center;
}


.input-fill:placeholder-shown::placeholder {
    color: transparent;
}
.input-lable {
    position: absolute;
    top: 20px;
    left: 0%;
    pointer-events: none;
    opacity: 1;
    transition-duration: 500ms;
    transition-timing-function: cubic-bezier(0, 0, 0.2, 1);
    transform:  translateY(-50%) ;
    transform: opacity;
    
}
.input-fill:not(:placeholder-shown) ~ .input-lable, 
.input-fill:focus ~ .input-lable {
    opacity: 0;
    transition-duration: 500ms;
    transition-timing-function: cubic-bezier(0, 0, 0.2, 1);
    transform:  translateY(50%) ;
    transform: opacity;
}
</style>