import Vue from "vue";
import Vuex from "vuex";
import VuexORM from "@vuex-orm/core";

// Import vuex-orm models
import {
  Place
} from "@/models";

// Import store modules
import PlaceModule from "./modules/place";

Vue.use(Vuex);

const database = new VuexORM.Database();

// Register vuex-orm models
database.register(Place);

const store = new Vuex.Store({
  state: {},
  actions: {},
  mutations: {},
  plugins: [VuexORM.install(database)],
  modules: {
    place: PlaceModule
  }
})

export default store