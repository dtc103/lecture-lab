<template>
    <MainPage v-if="page === 'main'" @switchPage="newPage => switchToUtility(newPage)" />
    <Summarize v-else-if="page === 'summarize'" @returnHome="returnHome()" />
    <Learn v-else-if="page === 'learn'" @returnHome="returnHome()" />
    <Ask v-else-if="page === 'ask'" @returnHome="returnHome()" />
    <NotAVideo v-else-if="page === 'novideo'" @returnHome="returnHome()" />
</template>

<script>
import MainPage from './components/MainPage.vue';
import Summarize from './components/Summarize.vue';
import Learn from './components/Learn.vue';
import Ask from './components/Ask.vue';
import NotAVideo from './components/NotAVideo.vue';

import { isOnVideoPage } from './lib';

export default {
  name: 'App',
  components: {
    MainPage,
    Summarize,
    Learn,
    Ask,
    NotAVideo
  },
  data() {
    return {
      page: 'main',
    }
  },
  methods: {
    async switchToUtility(utilityPage) {
      const isVideoPage = await isOnVideoPage();
      if (isVideoPage) {
        this.page = utilityPage;
      } else {
        this.page = 'novideo';
      }
    },
    returnHome() {
      this.page = 'main';
    }
  }
}
</script>

<style>
#app {
  font-family: 'Garamond', 'Georgia', serif;
  font-size: 15px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  width: 450px;
  height: 250px;
  background: white;
  border: solid black;
}

button {
  font-family: 'Garamond', 'Georgia', serif;
  font-size: 15px;
}
</style>
