// Author: ZHANG CHI
<template>
  <v-app>
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4" align="center" justify="center">
            <v-avatar color="" size="62">
              <img src="~/static/v.png" alt="logo" />
            </v-avatar>
            <v-card-title class="layout justify-center" disabled="true">
              ゆる～くつながる
            </v-card-title>
            <v-spacer></v-spacer>
            <v-expand-transition>
              <v-card v-show="expand" class="mx-auto">
                <v-form ref="form" v-model="valid" :lazy-validation="lazy">
                  <v-card-text>
                    <v-text-field
                      v-model="email"
                      id="email"
                      label="Maill Address"
                      name="email"
                      prepend-icon="mdi-account"
                      type="text"
                      :rules="emailRules"
                      required
                    ></v-text-field>
                  </v-card-text>
                  <v-card-text>
                    <v-text-field
                      v-model="password"
                      label="password"
                      name="password"
                      prepend-icon="mdi-lock"
                      type="password"
                      :rules="passwordRules"
                      required
                    ></v-text-field>
                  </v-card-text>
                </v-form>
              </v-card>
            </v-expand-transition>
            <v-snackbar v-model="snackbar">
              {{ text }}
            </v-snackbar>
            <v-card-actions class="layout justify-center">
              <v-btn
                v-if="registerflag"
                large
                color="red"
                class="layout justify-center"
                nuxt
                to="/register"
              >
                新規作成
              </v-btn>
              <v-btn
                v-if="loginflag"
                large
                color="red"
                class="layout justify-center"
                @click="login"
              >
                ログイン
              </v-btn>
            </v-card-actions>
            <v-divider></v-divider>
            <v-card-actions v-if="registerflag">
              <v-btn
                small
                color="gray"
                class="layout justify-center"
                @click="
                  (expand = !expand),
                    (loginflag = !loginflag),
                    (registerflag = !registerflag)
                "
              >
                ログイン
              </v-btn>
            </v-card-actions>
            <v-card-actions v-if="loginflag">
              <v-btn
                small
                color="gray"
                class="layout justify-center"
                nuxt
                to="/register"
              >
                新規作成
              </v-btn>
            </v-card-actions>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  layout: "login",
  data: () => ({
    valid: true,
    expand: false,
    loginflag: false,
    registerflag: true,
    lazy: false,
    email: "",
    emailRules: [
      v => !!v || "email is required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],
    password: "",
    passwordRules: [v => !!v || "password is required"],
    snackbar: false,
    text:
      "ログインに失敗しました。メールアドレスとパスワードがもう一度確認してください！",
    timeout: 2000
  }),
  methods: {
    login() {
      if (this.$refs.form.validate()) {
        let _this = this
        let email = this.email;
        let password = this.password;
        let errorflag = false;
        this.$axios({
          method: "post",
          url: "http://127.0.0.1:8000/users/login",
          data: { email: email, password: password }
        })
          .then(function(response) {
            if (response.data == null) {
              _this.snackbar = true;
            } else {
              console.log(response.data.email);
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    }
  }
};
</script>
