<!-- Author:Shun Kiyoura-->
<template>
  <v-layout column justify-center align-center>
    <v-container xs12 sm8 md6>
      <div class="text-center">
        <div id="chat-list">
          <v-list style="max-height: 550px" class="overflow-y-auto">
            <template v-for="(message, index) in messages">
              <v-list-item true :key="index" v-bind:id="index">
                <template v-if="message.user_id == userInfo.id">
                  <v-container fluid>
                    <v-row justify="end">
                      <v-col cols="5">
                        <v-card flat style="font-size:10px"
                          ><v-card color="#f5f5f5">
                            <v-card-text class="pa-2" style="font-size:14px">{{
                              message.content
                            }}</v-card-text> </v-card
                          ><v-container fluid
                            ><v-row justify="end" align="start">{{
                              message.created_at
                            }}</v-row></v-container
                          ></v-card
                        >
                      </v-col>
                      <v-col cols="2"
                        ><v-list-item-avatar
                          ><v-img
                            :src="avatar(message.user_id)"
                          ></v-img></v-list-item-avatar
                      ></v-col>
                    </v-row>
                  </v-container>
                </template>
                <template v-else>
                  <v-container fluid>
                    <v-row justify="start">
                      <v-col cols="2"
                        ><v-list-item-avatar
                          ><v-img
                            :src="avatar(message.user_id)"
                          ></v-img></v-list-item-avatar
                      ></v-col>
                      <v-col cols="5">
                        <v-card flat style="font-size:10px"
                          ><v-card color="#f5f5f5">
                            <v-card-text class="pa-2" style="font-size:14px">{{
                              message.content
                            }}</v-card-text> </v-card
                          ><v-container fluid
                            ><v-row justify="start" align="start">{{
                              message.created_at
                            }}</v-row></v-container
                          ></v-card
                        >
                      </v-col>
                    </v-row>
                  </v-container>
                </template>
              </v-list-item>
            </template>
          </v-list>
        </div>
        <v-row align="center"
          ><v-col cols="9"
            ><v-text-field
              color="deep-purple accent-3"
              v-model="send_message"
              label="Message"
            ></v-text-field></v-col
          ><v-col cols="3"
            ><v-btn color="white" class="deep-purple--text" @click="sendMessage"
              >send</v-btn
            ></v-col
          ></v-row
        >
      </div>
    </v-container>
  </v-layout>
</template>

<script>
import { mapState } from "vuex";
import moment from "moment/moment";
export default {
  layout: "_id",
  asyncData({ params }) {
    const { id } = params;
    return { chat_room_id: id };
  },
  data() {
    return {
      send_message: ""
    };
  },
  async created() {
    const _this = this;
    var ws = new WebSocket(`ws://localhost:8000/ws/${this.chat_room_id}`);
    ws.onmessage = function(event) {
      console.log("seeeeeeeentt!!!");
      _this.messages.push(JSON.parse(event.data));
      setTimeout(() => {
        let target = document.getElementById(_this.messages.length - 1);
        target.scrollIntoView();
      }, 0);
    };
  },
  methods: {
    sendMessage: async function(event) {
      var ws = new WebSocket(`ws://localhost:8000/ws/${this.chat_room_id}`);
      await this.$axios.post("/chats/", {
        user_id: this.$store.state.user.userInfo.id,
        chat_room_id: this.chat_room_id,
        content: this.send_message
      });
      var chat_data = {
        id: null,
        user_id: this.$store.state.user.userInfo.id,
        created_at: moment().format("HH:mm"),
        content: this.send_message,
        username: this.$store.state.user.userInfo.username
      };
      ws.send(JSON.stringify(chat_data));
      this.send_message = "";
      event.preventDefault();
    }
  },
  data: () => ({
    chat_room_id: null,
    messages: [],
    items: [
      { header: "Chat" },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg"
      },
      { divider: true, inset: true }
    ]
  }),
  computed: {
    ...mapState("user", ["userInfo"]),
    avatar() {
      return id => {
        const imageLen = 10;
        return `/user_icon_${(id % imageLen) + 1}.jpg`;
      };
    }
  },

  async mounted() {
    const res = await this.$axios.get("/chats", {
      params: {
        chat_room_id: this.chat_room_id
      }
    });
    this.messages = res.data;

    setTimeout(() => {
      let target = document.getElementById(this.messages.length - 1);
      target.scrollIntoView();
    }, 0);
  }
};
</script>
