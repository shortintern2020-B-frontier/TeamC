<!-- Author:Shun Kiyoura-->
<template>
  <v-layout column justify-center align-center>
    <v-container xs12 sm8 md6>
      <div class="text-center">
        <v-list style="max-height: 450px" class="overflow-y-auto">
          <template v-for="(message) in messages">
            <v-list-item true :key="message.content">
              <template v-if="message.user_id == userInfo.id">
                <v-list-item-content >
                  <v-list-item-subtitle v-html="message.content"></v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-avatar>
                  <v-img :src="avatar(message.user_id)"></v-img>
                </v-list-item-avatar>
              </template>
              <template v-else>
                <v-list-item-avatar>
                  <v-img :src="avatar(message.user_id)"></v-img>
                </v-list-item-avatar>
                <v-list-item-content >
                  <v-list-item-subtitle v-html="message.content"></v-list-item-subtitle>
                </v-list-item-content>
              </template>
            </v-list-item>
          </template>
        </v-list>
        <v-text-field v-model="send_message" label="Message"></v-text-field>
        <v-btn @click="sendMessage">send</v-btn>
      </div>
    </v-container>
  </v-layout>
</template>

<script>
import { mapState } from 'vuex';
import moment from 'moment/moment'
export default {
  layout: "_id",
  asyncData({ params }) {
    const { id } = params;
    return { chat_room_id: id };
  },
  data() {
    return {
      send_message: ''
    };
  },
  async created() {
    const res = await this.$axios.get("/chats", {
      params: {
        chat_room_id: this.chat_room_id,
      },
    });
    this.messages = res.data;
 
    const _this = this;
    var ws = new WebSocket(`ws://localhost:8000/ws/${this.chat_room_id}`);
    ws.onmessage = function(event) {
      console.log("seeeeeeeentt!!!");
      _this.messages.push(JSON.parse(event.data));
    };
  },
  methods: {
    sendMessage: async function (event) {
      var ws = new WebSocket(`ws://localhost:8000/ws/${this.chat_room_id}`);
      await this.$axios.post("/chats/", {
        user_id: this.$store.state.user.userInfo.id,
        chat_room_id: this.chat_room_id,
        content: this.send_message
      });
      var chat_data = {
        "id": null,
        "user_id": this.$store.state.user.userInfo.id,
        "created_at": moment().format("YYYY/MM/DD HH:MM"),
        "content": this.send_message,
        "username": this.$store.state.user.userInfo.username
      }
      ws.send(JSON.stringify(chat_data))
      this.send_message = ""
      event.preventDefault()
    },
  },
  data: () => ({
    chat_room_id: null,
    messages: [],
    items: [
      { header: "Chat" },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        },
      { divider: true, inset: true }
    ],
  }),
  computed: {
    ...mapState('user', ['userInfo']),
    avatar() {
      return (id) => {
        console.log(id)
        const imageLen = 10;
        return `/user_icon_${id % imageLen + 1}.jpg`;
      }
    }
  }
};
</script>
