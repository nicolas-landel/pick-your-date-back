import { Model } from "@vuex-orm/core";

export class Place extends Model {
  static primaryKey = "uuid";
  static entity = "places";

  static fields() {
    return {
      uuid: this.uid(""),
      updatedAt: this.attr(),
      createdAt: this.attr(),
    };
  }
}