import { BaseModel } from "./baseModels";

export class Place extends BaseModel {
  static entity = "places";

  static fields() {
    return {
      ...super.fields(),
    };
  }
}