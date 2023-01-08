import { Model } from "@vuex-orm/core";

export class BaseModel extends Model {
  static primaryKey = "uuid";

  static fields() {
    return {
      uuid: this.uid(""),
      updatedAt: this.attr(),
      createdAt: this.attr(),
    };
  }
}