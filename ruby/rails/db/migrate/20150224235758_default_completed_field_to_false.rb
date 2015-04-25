class DefaultCompletedFieldToFalse < ActiveRecord::Migration
  def change
    change_column :todos, :completed, :boolean, :default => false
  end
end
