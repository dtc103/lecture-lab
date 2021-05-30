<template>
  <div class="container">
    <header>
      <img class="logo" src="../assets/logo.png">
      <h2>Lecture Lab</h2>
    </header>
    <div class="actions">
      
      <ImageButton @click="switchPage('summarize')" imgName="summarize.png" title="Summarize" />
      <ImageButton @click="switchPage('learn')" imgName="learn.png" title="Learn" />
      <ImageButton @click="switchPage('ask')" imgName="ask.png" title="Ask" />
    </div>
  </div>
</template>

<script>
import ImageButton from './ImageButton';

export default {
  name: 'MainPage',
  components: {
    ImageButton
  },
  methods: {
    switchPage(page) {
      this.$emit('switchPage', page);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.logo {
  width: 40px;
}

.container {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}

.actions {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

</style>
