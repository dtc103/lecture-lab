<template>
    <div class="container">
        <LoadingSpinner class="spinner" v-if="loading" />
        <div v-else-if="questionAnswerPairs.length > 0" class="flashcard-area">
            <img :class="{ arrow: true, disabled: currentPairIndex === 0 }" @click="goLeft()" src="@/assets/left.png">
            <div class="question-answer-area">
                {{ currentQuestion }}
                <br />
                <span class="answer">{{ currentAnswer }}</span>
            </div>
            <img :class="{ arrow: true, disabled: currentPairIndex === questionAnswerPairs.length - 1 }" @click="goRight()" src="@/assets/right.png">
        </div>
        <div class="buttons">
            <ImageButton @click="refreshQuestionAnswerPairs()" imgName="retry.png" title="Retry" />
            <ImageButton @click="null" imgName="download.png" title="Export" />
            <ImageButton @click="$emit('returnHome')" imgName="exit.png" title="Back" />
        </div>
    </div>
</template>
<script>
import { getCurrentVideoId, generateQuestionAnswerPairs } from '../lib';
import ImageButton from './ImageButton';
import LoadingSpinner from './LoadingSpinner';

export default {
    name: 'Learn',
    components: {
        ImageButton,
        LoadingSpinner
    },
    data() {
        return {
            currentPairIndex: 0,
            questionAnswerPairs: [],
            loading: false
        }
    },
    computed: {
        currentQuestion() {
            if (this.questionAnswerPairs.length === 0) {
                return null;
            }
            return this.questionAnswerPairs[this.currentPairIndex].question;
        },
        currentAnswer() {
            if (this.questionAnswerPairs.length === 0) {
                return null;
            }
            return this.questionAnswerPairs[this.currentPairIndex].answer;
        }
    },
    mounted() {
        this.refreshQuestionAnswerPairs();
    },
    methods: {
        async refreshQuestionAnswerPairs() {
            this.loading = true;

            const videoId = await getCurrentVideoId();
            const qaPairs = await generateQuestionAnswerPairs(videoId);

            this.questionAnswerPairs = qaPairs;
            this.loading = false;
        },
        goLeft() {
            this.currentPairIndex = Math.max(this.currentPairIndex - 1, 0);
        },
        goRight() {
            this.currentPairIndex = Math.min(this.currentPairIndex + 1, this.questionAnswerPairs.length - 1);
        }
    }
}
</script>
<style scoped>
    .arrow {
        width: 30px;
        cursor: pointer;
    }

    .arrow.disabled {
        opacity: 0.5;
        cursor: default;
    }

    .flashcard-area {
        display: flex;

        align-items: center;
        justify-content: space-evenly;
    }

    .question-answer-area {
        width: 60%
    }

    .answer {
        filter: blur(3.5px);
    }

    .answer:hover {
        filter: none;
        cursor: none;
    }

    .spinner {
        margin-left: auto;
        margin-right: auto;
    }

    .container {
        overflow: auto;
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        height: 100%;
    }

    .buttons {
        display: flex;
        align-items: center;
        justify-content: space-evenly;
    }
</style>