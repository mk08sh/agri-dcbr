<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Renewal</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!--Name Section  -->
              <v-layout mx-2 mt-2>
                <h4>Operator's Name</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="firstName"
                    :rules="nameRules"
                    label="First name"
                    name="firstName"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="middleName"
                    :rules="nameRules"
                    label="Middle name (optional)"
                    name="middleName"
                  ></v-text-field>
                </v-flex>

                <v-flex xs12 md4>
                  <v-text-field
                    v-model="lastName"
                    :rules="nameRules"
                    label="Last name"
                    name="lastName"
                    required
                  ></v-text-field>
                </v-flex>
              </v-layout>

              <v-layout mx-2 mt-2>
                <h4>Registration Record</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field :rules="nameRules" label="Reg #" name="firstName" required></v-text-field>
                </v-flex>

                <v-flex xs12 md4>
                  <DatePicker />
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import DatePicker from "@/components/DatePicker";
import { mapState } from "vuex";
export default {
  components: {
    DatePicker
  },
  data: () => ({
    valid: false,
    mask: "",

    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ],
    streetNumberRules: [v => !!v || "Street number is required"]
  }),

  computed: {
    ...mapState({
      profile: state => state.profile
    }),
    firstName: {
      // getter
      get() {
        return this.$store.getters["profile/firstName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/firstName", value);
      }
    },

    middleName: {
      // getter
      get() {
        return this.$store.getters["profile/middleName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/middleName", value);
      }
    },
    lastName: {
      // getter
      get() {
        return this.$store.getters["profile/lastName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/lastName", value);
      }
    },
    commType: {
      // getter
      get() {
        return this.$store.getters["profile/commType"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/commType", value);
      }
    },
    phone: {
      // getter
      get() {
        return this.$store.getters["profile/phone"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/phone", value);
      }
    },
    email: {
      // getter
      get() {
        return this.$store.getters["profile/email"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/email", value);
      }
    },
    streetNumber: {
      // getter
      get() {
        return this.$store.getters["profile/streetNumber"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/streetNumber", value);
      }
    },
    aptNumber: {
      // getter
      get() {
        return this.$store.getters["profile/aptNumber"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/aptNumber", value);
      }
    },
    streetName: {
      // getter
      get() {
        return this.$store.getters["profile/streetName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/streetName", value);
      }
    },
    city: {
      // getter
      get() {
        return this.$store.getters["profile/city"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/city", value);
      }
    },
    postalCode: {
      // getter
      get() {
        return this.$store.getters["profile/postalCode"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/postalCode", value);
      }
    },
    homeAsOperation: {
      // getter
      get() {
        return this.$store.getters["profile/homeAsOperation"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/homeAsOperation", value);
      }
    }
  }
};
</script>
