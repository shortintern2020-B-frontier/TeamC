<!-- Author:Shun Kiyoura-->
<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <div class="text-center">
        <v-list style="max-height: 500px" class="overflow-y-auto">
          <template v-for="(message) in messages">
            <v-list-item true :key="message.content">
              <v-list-item-avatar>
                <v-img :src="items[1].avatar"></v-img>
              </v-list-item-avatar>
              <v-list-item-content > <!--style="height: 200px"-->
                <v-list-item-subtitle v-html="message.content"></v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
        <v-text-field v-model="send_message" label="Message"></v-text-field>
        <v-btn @click="sendMessage">send</v-btn>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import moment from 'moment/moment'
export default {
  asyncData({ params }) {
    const { id } = params;
    return { chat_room_id: id };
  },
  
  async created() {
    const res = await this.$axios.get("/chats", {
      params: {
        chat_room_id: 1,//this.chat_room_id,
      },
    }); 
    const _this = this;
    this.messages = res.data;

    var ws = new WebSocket(`ws://localhost:8000/ws/1`);
    ws.onmessage = function(event) {

                /*var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)*/

                //リスト更新の処理を書く
                console.log("seeeeeeeentt!!!");
                _this.messages.push(JSON.parse(event.data));
    };
    
  },
    methods: {
    sendMessage: async function (event) {
      var ws = new WebSocket(`ws://localhost:8000/ws/1`);
      console.log(this.send_message);
      await this.$axios.post("/chats/", {
        user_id: 1,//this.$store.state.user.userInfo.id,
        chat_room_id: 1,//this.chat_room_id,
        content: this.send_message
      });
      var chat_data = {
        "id": null,
        "user_id": 1,//this.userInfo.id,
        "created_at": moment().format("YYYY/MM/DD HH:MM"),
        "content": this.send_message,
        "username": "shun"//this.userInfo.username
      }
      ws.send(JSON.stringify(chat_data))
      this.send_message = ""
      event.preventDefault()
    },
  },
  data: () => ({
    chat_room_id: 1,
    messages: [],
    items: [
      { header: "Chat" },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        },
      { divider: true, inset: true }
    ],
  }),
};
</script>
